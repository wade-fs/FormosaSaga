// /std/site.c
//
// 《源流福爾摩沙》核心地點容器。
// 取代傳統 MUD 的 /std/room.c。
//
// 繼承關係：
//   entity.c     → 身份、屬性、事件發送
//   reveal_layer.c → 條件顯示層
//
// 每個 site 代表一個「地點」，可以是：
//   - 一個行政聚落（民雄鄉）
//   - 一個歷史場景（台北城門・乙未）
//   - 一個文化地標（霧社公學校）
//
// 不繼承傳統 room.c 的原因：
//   room.c 假設固定出口、固定描述、固定行為。
//   site.c 的描述是動態的，出口是語意的（travel 指令），
//   行為取決於玩家的理解深度。
//
// Canon 參照：
//   docs/mudlib/02_domain_model.md（Site Aggregate）
//   docs/mudlib/03_world_engine.md（語意層）

#include "/include/formosa.h"

inherit "/std/entity.c";
inherit "/std/reveal_layer.c";

// ── 靜態設定（由 YAML 載入，或子類 create() 設定）────────
private string base_description;     // 所有人都看得見的基礎描述
private string era_id;               // 所屬歷史時代（現代場景為 "modern"）
private string settlement_id;        // 所屬聚落 id
private int    is_heritage;          // 1=歷史保護區，禁止破壞性操作
private mapping neighbors;           // 鄰近可 travel 的地點
                                     // ([ "方向描述": "site_or_settlement_id" ])

// ── 玩家追蹤 ──────────────────────────────────────────
private nosave mapping occupants;    // ([ player_id: player_ob ])

// ── 生命週期 ──────────────────────────────────────────
void create() {
    entity::create();
    reveal_layer::create();
    occupants  = ([]);
    neighbors  = ([]);
    is_heritage = 0;
    era_id     = "modern";
    set_entity_type("site");
}

// ── 靜態設定 API ──────────────────────────────────────
void set_base_description(string desc) { base_description = desc; }
void set_era_id(string id)             { era_id = id; }
void set_settlement_id(string id)      { settlement_id = id; }
void set_heritage(int val)             { is_heritage = val; }

string query_era_id()        { return era_id; }
string query_settlement_id() { return settlement_id; }
int    query_is_heritage()   { return is_heritage; }

// 鄰居（travel 目標）
void add_neighbor(string direction_label, string target_id) {
    neighbors[direction_label] = target_id;
}
mapping query_neighbors() { return copy(neighbors); }

// ── 玩家進出 ──────────────────────────────────────────
void player_enter(object player) {
    if (!player || !userp(player)) return;

    string pid = player->query_entity_id();
    occupants[pid] = player;

    // 記錄回程（供 travel 返回使用）
    string prev = player->query_temp("current_site_id");
    if (prev && prev != query_entity_id())
        player->set_temp("previous_site_id", prev);
    player->set_temp("current_site_id", query_entity_id());

    // 授予地理踏印（委託給 FOOTPRINT_D）
    catch(FOOTPRINT_D->on_player_enter_site(player, this_object()));

    // 通知其他在場者
    _tell_others(player,
        player->query_display_name() + " 來到了這裡。\n");

    // 推送 look 給進入的玩家
    call_out("do_look", 0, player);

    // 發送事件
    emit("PlayerEnteredSite", ([
        "player_id":   pid,
        "site_id":     query_entity_id(),
        "era_id":      era_id,
    ]));
}

void player_leave(object player) {
    if (!player) return;
    string pid = player->query_entity_id();
    m_delete(occupants, pid);

    _tell_others(player,
        player->query_display_name() + " 離開了。\n");

    emit("PlayerLeftSite", ([
        "player_id": pid,
        "site_id":   query_entity_id(),
    ]));
}

mapping query_occupants() { return copy(occupants); }

// ── LOOK：核心顯示邏輯 ────────────────────────────────
//
// 組合三個來源：
//   1. base_description（所有人都看見）
//   2. settlement 動態數值（記憶完整度、失源者狀態）
//   3. reveal_layer 的條件浮現內容
//
void do_look(object player) {
    if (!player || !userp(player)) return;

    string out = "";

    // ── 標題 ──
    out += C_TITLE + "【" + ERA_D->resolve_name(clean_id, query_entity_type(), player) + "】" + C_RESET + "\n";

    // ── 基礎描述 ──
    if (base_description && base_description != "")
        out += base_description + "\n";

    // ── 條件浮現層 ──
    mapping revealed = resolve_reveals(player);

    // 浮現文字（按順序附加，每段空一行）
    if (sizeof(revealed["texts"])) {
        out += "\n";
        foreach (string txt in revealed["texts"])
            out += txt + "\n";
    }

    // 浮現 NPC
    if (sizeof(revealed["npcs"])) {
        out += "\n";
        foreach (string npc_id in revealed["npcs"]) {
            string npc_name = NPC_D->query_npc_name(npc_id);
            string npc_hint = NPC_D->query_npc_hint(npc_id);
            if (npc_name)
                out += C_DIM + npc_name + C_RESET;
            if (npc_hint)
                out += " — " + npc_hint;
            out += "\n";
        }
    }

    // ── 聚落記憶狀態 ──
    if (settlement_id) {
        int mem = SETTLEMENT_D->query_dim(settlement_id, DIM_MEMORY);
        out += "\n";

        if (mem >= 60)
            out += C_GOOD;
        else if (mem >= OBLIVION_WARN)
            out += C_MEMORY;
        else
            out += C_WARN;

        out += "記憶完整度：" + mem + "%" + C_RESET;

        // 失源者提示
        mixed *specters = SETTLEMENT_D->query_active_specters(settlement_id);
        if (sizeof(specters)) {
            out += "　" + C_WARN +
                   "有什麼東西正在消失。" +
                   C_RESET;
        }

        out += "\n";
    }

    // ── 歷史層入口 ──
    if (sizeof(revealed["entries"])) {
        out += "\n" + C_HISTORY + "【歷史層可見】" + C_RESET + "\n";
        int idx = 1;
        foreach (mapping entry in revealed["entries"]) {
            out += "  " + idx + ". " + entry["label"] + "\n";
            idx++;
        }
        out += C_DIM +
               "輸入 enter <編號> 進入歷史層。" +
               C_RESET + "\n";
        // 把入口列表暫存給玩家（供 enter 指令使用）
        player->set_temp("history_entries", revealed["entries"]);
    }

    // ── 可前往的鄰近地點 ──
    string clean_id = query_entity_id();
    int colon_idx = strsrch(clean_id, ":");
    if (colon_idx != -1) {
        clean_id = substr(clean_id, colon_idx + 1, strlen(clean_id) - colon_idx - 1);
    }

    string *conns = ROUTE_D->query_connections(clean_id);
    if (sizeof(conns)) {
        out += "\n" + C_DIM + "可前往：" + C_RESET;
        string *conn_names = ({});
        foreach (string target_id in conns) {
            string resolved = ERA_D->resolve_name(target_id, "site", player);
            conn_names += ({ resolved });
        }
        out += implode(conn_names, "、") + "\n";
        out += C_DIM + "輸入 travel <地名> 出發。" + C_RESET + "\n";
    }

    tell_object(player, out);

    // 浮現記憶碎片（觸發但不直接顯示，讓 MEMORY_D 處理通知）
    if (sizeof(revealed["memories"])) {
        foreach (string mid in revealed["memories"])
            catch(MEMORY_D->on_fragment_accessible(player, mid));
    }
}

// ── TRAVEL 指令處理 ───────────────────────────────────
//
// 玩家輸入 travel 嘉義市，系統找到對應 id，執行移動。
//
int do_travel(object player, string destination) {
    string target_id = 0;
    string clean_id = query_entity_id();
    int colon_idx = strsrch(clean_id, ":");
    if (colon_idx != -1) {
        clean_id = substr(clean_id, colon_idx + 1, strlen(clean_id) - colon_idx - 1);
    }

    string *conns = ROUTE_D->query_connections(clean_id);

    foreach (string tid in conns) {
        string resolved = ERA_D->resolve_name(tid, "site", player);
        if (lower_case(resolved) == lower_case(destination) ||
            strsrch(resolved, destination) != -1 ||
            lower_case(tid) == lower_case(destination) ||
            strsrch(tid, destination) != -1) {
            target_id = tid;
            break;
        }
    }

    if (!target_id) {
        tell_object(player,
            C_WARN + "找不到「" + destination + "」。" + C_RESET +
            "輸入 look 查看可前往的地點。\n");
        return 0;
    }

    // 過場文字（由目標 site 提供，或使用預設）
    object target_ob = SETTLEMENT_D->get_site_object(target_id);
    if (!target_ob) {
        tell_object(player, C_WARN + "那個地方現在無法前往。\n" + C_RESET);
        return 0;
    }

    string travel_text = target_ob->query_prop("travel_arrive_text");
    if (!travel_text)
        travel_text = "你前往了" + ERA_D->resolve_name(target_id, "site", player) + "。";

    tell_object(player, "\n" + travel_text + "\n");

    // 執行移動
    player_leave(player);
    target_ob->player_enter(player);

    return 1;
}

// ── ENTER：進入歷史層 ─────────────────────────────────
int do_enter_history(object player, int index) {
    mixed *entries = player->query_temp("history_entries");
    if (!entries || !sizeof(entries)) {
        tell_object(player, "這裡沒有可進入的歷史層。\n");
        return 0;
    }

    index--;  // 轉為 0-based
    if (index < 0 || index >= sizeof(entries)) {
        tell_object(player, "請輸入正確的編號。\n");
        return 0;
    }

    mapping entry  = entries[index];
    string  era    = entry["era"];
    string  s_id   = settlement_id;

    // 委託給 TIMELINE_D 找到對應的歷史層 site 物件
    object history_site = TIMELINE_D->get_history_site(s_id, era);
    if (!history_site) {
        tell_object(player,
            C_WARN + "歷史層尚未開啟，或需要更多記憶才能進入。\n" + C_RESET);
        return 0;
    }

    tell_object(player,
        "\n" + C_HISTORY +
        "記憶的縫隙在你眼前展開——\n" +
        C_RESET);

    player_leave(player);
    history_site->player_enter(player);

    emit("PlayerEnteredHistoryLayer", ([
        "player_id": player->query_entity_id(),
        "era_id":    era,
        "site_id":   query_entity_id(),
    ]));

    return 1;
}

// ── 工具 ──────────────────────────────────────────────
private void _tell_others(object except_ob, string msg) {
    foreach (string pid, object p in occupants) {
        if (p && p != except_ob)
            tell_object(p, msg);
    }
}

// 供外部查詢
int    query_is_site()  { return 1; }
string query_short()    { return query_display_name(); }

void look_room(object player) {
    do_look(player);
}

mixed query_exits() { return 0; }
string look_at_item(string id) { return ""; }

