// /daemon/settlement_d.c
//
// 聚落守護進程。
//
// 職責：
//   - 載入聚落靜態設定（YAML）
//   - 管理聚落六維動態數值（JSON 存檔）
//   - 判定升級、失源者生成
//   - 提供 site 物件的查詢與載入
//
// 設計原則：
//   Daemon 只做協調與計算，不持有主體狀態。
//   狀態由各聚落的 .o 存檔持有，Daemon 是計算服務。
//
// Canon 參照：
//   docs/mudlib/02_domain_model.md（SettlementService）
//   docs/mudlib/05_data_storage.md（Entity Hydration Pattern）

#include "/include/formosa.h"

inherit "/std/entity.c";

// ── 記憶體快取 ────────────────────────────────────────
// 已載入的聚落執行期狀態
// ([ settlement_id: runtime_mapping ])
private nosave mapping active_settlements;

// 已載入的 site 物件
// ([ site_id: site_object ])
private nosave mapping active_sites;

void create() {
    entity::create();
    set_entity_id("daemon:settlement");
    set_entity_type("daemon");
    active_settlements = ([]);
    active_sites       = ([]);

    // 訂閱踏印事件，更新聚落記憶值
    catch(EVENT_D->subscribe("FootprintGained",    "on_footprint_gained"));
    catch(EVENT_D->subscribe("MemoryCompleted",    "on_memory_completed"));
    catch(EVENT_D->subscribe("SpecterResolved",    "on_specter_resolved"));
}

// ── 載入聚落（Entity Hydration Pattern）──────────────
mapping load_settlement(string id) {
    if (active_settlements[id]) return active_settlements[id];

    // 1. 靜態 YAML
    string yaml_path = YAML_SETTLEMENTS + id + ".yaml";
    if (file_size(yaml_path) <= 0) {
        log_file("settlement_errors.log",
            sprintf("[%s] 找不到聚落 YAML：%s\n", ctime(time()), yaml_path));
        return 0;
    }

    mapping static_data = yaml_decode(read_file(yaml_path));
    if (!static_data) return 0;

    mapping runtime = copy(static_data);

    // 2. 動態存檔覆蓋
    string save_path = STATE_SETTLEMENTS + id;
    if (file_size(save_path + ".o") > 0) {
        object helper = clone_object("/std/entity.c");
        if (helper) {
            if (helper->restore_object(save_path)) {
                // 只覆蓋六維動態數值
                foreach (string dim in ({
                    DIM_POPULATION, DIM_INDUSTRY, DIM_CULTURE,
                    DIM_MEMORY, DIM_TRADE, DIM_COHESION
                })) {
                    mixed val = helper->query_prop(dim);
                    if (intp(val)) runtime[dim] = val;
                }
                // 失源者列表
                mixed sp = helper->query_prop("specters_active");
                if (sp) runtime["specters_active"] = sp;
            }
            destruct(helper);
        }
    } else {
        _save_settlement(id, runtime);
    }

    active_settlements[id] = runtime;
    return runtime;
}

// ── 六維 API ─────────────────────────────────────────
int query_dim(string settlement_id, string dim) {
    mapping s = load_settlement(settlement_id);
    if (!s) return 0;
    return s[dim] || 0;
}

// delta 可正可負
int add_dim(string settlement_id, string dim, int delta) {
    mapping s = load_settlement(settlement_id);
    if (!s) return 0;

    int old_val = s[dim] || 0;
    int new_val = old_val + delta;
    if (new_val < 0)   new_val = 0;
    if (new_val > 100) new_val = 100;

    s[dim] = new_val;
    _save_settlement(settlement_id, s);

    emit("SettlementChanged", ([
        "settlement_id": settlement_id,
        "dim":           dim,
        "old_value":     old_val,
        "new_value":     new_val,
    ]));

    // 記憶值變動時，檢查失源者
    if (dim == DIM_MEMORY)
        _check_oblivion(settlement_id, new_val);

    // 檢查升級條件
    _check_upgrade(settlement_id);

    return new_val;
}

// 直接設定（供初始化或 GM 使用）
void set_dim(string settlement_id, string dim, int val) {
    mapping s = load_settlement(settlement_id);
    if (!s) return;
    if (val < 0)   val = 0;
    if (val > 100) val = 100;
    s[dim] = val;
    _save_settlement(settlement_id, s);
}

// ── 失源者管理 ────────────────────────────────────────
mixed *query_active_specters(string settlement_id) {
    mapping s = load_settlement(settlement_id);
    if (!s) return ({});
    return s["specters_active"] || ({});
}

private void _check_oblivion(string settlement_id, int memory_val) {
    if (memory_val < OBLIVION_SPECTER) {
        // 判斷失源者型態（依記憶子項目最低者）
        // 簡化版：直接生成失史者，完整版應檢查子項目
        _spawn_specter(settlement_id, SP_LOST_HISTORY);
    } else if (memory_val < OBLIVION_WARN) {
        emit("OblivionRising", ([
            "settlement_id": settlement_id,
            "memory_val":    memory_val,
        ]));
    }
}

private void _spawn_specter(string settlement_id, string specter_type) {
    mapping s = load_settlement(settlement_id);
    if (!s) return;

    mixed *existing = s["specters_active"] || ({});

    // 避免重複生成同型態失源者
    foreach (mapping sp in existing)
        if (sp["type"] == specter_type) return;

    string specter_id = sprintf("SP_%s_%s_%d",
        settlement_id, specter_type, time());

    mapping specter = ([
        "id":   specter_id,
        "type": specter_type,
        "born": time(),
    ]);

    s["specters_active"] = existing + ({ specter });
    _save_settlement(settlement_id, s);

    emit("SpecterSpawned", ([
        "settlement_id": settlement_id,
        "specter_id":    specter_id,
        "specter_type":  specter_type,
    ]));
}

void resolve_specter(string settlement_id, string specter_id, object player) {
    mapping s = load_settlement(settlement_id);
    if (!s) return;

    mixed *existing = s["specters_active"] || ({});
    mixed *remaining = ({});
    foreach (mapping sp in existing)
        if (sp["id"] != specter_id) remaining += ({ sp });

    s["specters_active"] = remaining;
    _save_settlement(settlement_id, s);

    emit("SpecterResolved", ([
        "settlement_id": settlement_id,
        "specter_id":    specter_id,
        "resolver":      player ? player->query_entity_id() : "system",
    ]));
}

// ── 升級判定 ──────────────────────────────────────────
private void _check_upgrade(string settlement_id) {
    mapping s = load_settlement(settlement_id);
    if (!s) return;

    int tier = s["tier"] || TIER_VILLAGE;

    // 村級 → 3級城
    if (tier == TIER_VILLAGE &&
        s[DIM_MEMORY]   >= 60 &&
        s[DIM_CULTURE]  >= 50 &&
        s[DIM_COHESION] >= 50) {

        s["tier"] = TIER_CITY3;
        _save_settlement(settlement_id, s);
        emit("SettlementUpgraded", ([
            "settlement_id": settlement_id,
            "from_tier": TIER_VILLAGE,
            "to_tier":   TIER_CITY3,
        ]));
    }
}

// ── Site 物件管理 ─────────────────────────────────────
object get_site_object(string site_id) {
    if (active_sites[site_id] && objectp(active_sites[site_id]))
        return active_sites[site_id];

    // 嘗試載入對應的 LPC 物件
    // 慣例：site_id "minxiong" → /area/settlements/minxiong.c
    string path = "/area/settlements/" + site_id + ".c";
    if (file_size(path) <= 0)
        path = "/area/sites/" + site_id + ".c";
    if (file_size(path) <= 0) return 0;

    object ob = catch(load_object(path));
    if (ob) active_sites[site_id] = ob;
    return ob;
}

// ── 事件回呼 ──────────────────────────────────────────
void on_footprint_gained(mapping event) {
    mapping data        = event["data"];
    string  footprint_id = data["footprint_id"];
    string  category    = data["category"];

    // 從踏印 id 解析所屬聚落（慣例：geo:minxiong:... 或 FOOTPRINT_D 提供）
    string s_id = catch(FOOTPRINT_D->query_footprint_settlement(footprint_id));
    if (!s_id) return;

    // 地理踏印 → 記憶 +3、文化 +1
    if (category == FP_GEO) {
        add_dim(s_id, DIM_MEMORY,  3);
        add_dim(s_id, DIM_CULTURE, 1);
    }
    // 人情踏印 → 凝聚 +3、記憶 +2
    if (category == FP_RELATION) {
        add_dim(s_id, DIM_COHESION, 3);
        add_dim(s_id, DIM_MEMORY,   2);
    }
    // 技藝踏印 → 文化 +3、產業 +1
    if (category == FP_CRAFT) {
        add_dim(s_id, DIM_CULTURE,  3);
        add_dim(s_id, DIM_INDUSTRY, 1);
    }
    // 聚落踏印 → 記憶 +5（最直接）
    if (category == FP_SETTLEMENT) {
        add_dim(s_id, DIM_MEMORY, 5);
    }
}

void on_memory_completed(mapping event) {
    mapping data = event["data"];
    string s_id  = data["settlement_id"];
    if (!s_id) return;
    // 記憶完成 → 記憶 +8
    add_dim(s_id, DIM_MEMORY, 8);
}

void on_specter_resolved(mapping event) {
    mapping data = event["data"];
    string s_id  = data["settlement_id"];
    if (!s_id) return;
    // 失源者解除 → 記憶回升 +10
    add_dim(s_id, DIM_MEMORY, 10);
}

// ── 存檔（只存動態數值）──────────────────────────────
private void _save_settlement(string id, mapping data) {
    string save_path = STATE_SETTLEMENTS + id;
    if (file_size(STATE_SETTLEMENTS) < 0)
        catch(mkdir(STATE_SETTLEMENTS));

    object helper = clone_object("/std/entity.c");
    if (!helper) return;

    foreach (string dim in ({
        DIM_POPULATION, DIM_INDUSTRY, DIM_CULTURE,
        DIM_MEMORY, DIM_TRADE, DIM_COHESION
    }))
        helper->set_prop(dim, data[dim] || 0);

    helper->set_prop("specters_active", data["specters_active"] || ({}));
    helper->set_prop("tier", data["tier"] || TIER_VILLAGE);

    catch(helper->save_object(save_path));
    destruct(helper);
}
