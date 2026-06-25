// /daemon/settlement_d.c
#include "/include/ansi.h"

inherit "/std/object";

// 記憶體中的即時狀態：([ "settlement_id": runtime_mapping ])
private nosave mapping active_settlements;

// 用於存檔與讀檔的臨時欄位 (非 nosave 變數，會被 save_object 存檔)
int population;
int memory;
int culture;
int trade;
int cohesion;

// 驗證聚落資料結構
int validate_settlement(mapping data) {
    if (!data || !mapp(data)) return 0;
    
    // 檢查必要字串欄位
    if (!stringp(data["id"]) || !stringp(data["name"]) || !stringp(data["level"])) {
        log_file("validation_errors.log", sprintf("聚落驗證失敗: id, name, 或 level 缺失或非字串\n"));
        return 0;
    }
    
    // 檢查數值欄位是否合理
    if (data["population"] < 0) {
        log_file("validation_errors.log", sprintf("聚落 %s (%s) 驗證失敗: 人口數 population 為負值 (%d)\n", data["name"], data["id"], data["population"]));
        return 0;
    }
    if (data["memory"] < 0 || data["culture"] < 0 || data["trade"] < 0 || data["cohesion"] < 0) {
        log_file("validation_errors.log", sprintf("聚落 %s (%s) 驗證失敗: 記憶/文化/貿易/凝聚力值不能為負數\n", data["name"], data["id"]));
        return 0;
    }

    // 檢查產業 (必須是字串陣列)
    if (data["industry"]) {
        if (!pointerp(data["industry"])) {
            log_file("validation_errors.log", sprintf("聚落 %s (%s) 驗證失敗: industry 欄位必須是陣列\n", data["name"], data["id"]));
            return 0;
        }
        foreach (mixed ind in data["industry"]) {
            if (!stringp(ind)) {
                log_file("validation_errors.log", sprintf("聚落 %s (%s) 驗證失敗: 產業名稱包含非字串元素\n", data["name"], data["id"]));
                return 0;
            }
        }
    }

    return 1;
}

// 取得或加載聚落實體 (Entity Hydration Pattern)
mapping load_settlement(string id) {
    if (!id || id == "") return 0;
    if (active_settlements[id]) {
        return active_settlements[id];
    }

    string yaml_path = sprintf("/world/settlements/%s.yaml", id);
    string save_path = sprintf("/data/state/settlements/%s", id); // 不加 .o

    // 1. 載入靜態設定
    if (file_size(yaml_path) <= 0) {
        log_file("storage_errors.log", "找不到聚落 YAML 設定: " + yaml_path + "\n");
        return 0;
    }
    
    string yaml_content = read_file(yaml_path);
    mapping static_data = yaml_decode(yaml_content);
    if (!static_data) {
        log_file("storage_errors.log", "YAML 解析失敗: " + yaml_path + "\n");
        return 0;
    }

    // 進行聚落資料結構驗證
    if (!validate_settlement(static_data)) {
        log_file("storage_errors.log", "聚落靜態 YAML 驗證失敗: " + yaml_path + "\n");
        return 0;
    }

    // 2. 初始化執行期狀態（以靜態資料為底）
    mapping runtime_data = copy(static_data);

    // 3. 嘗試融合動態存檔 (防目錄不存在)
    if (file_size("/data/state/settlements/") < 0) {
        mkdir("/data/state/settlements/");
    }

    if (file_size(save_path + ".o") > 0) {
        if (restore_object(save_path)) {
            // 將存檔內的動態欄位覆蓋至執行期狀態
            runtime_data["population"] = population;
            runtime_data["memory"]     = memory;
            runtime_data["culture"]    = culture;
            runtime_data["trade"]      = trade;
            runtime_data["cohesion"]   = cohesion;
        }
        // 清空暫存，避免記憶體殘留
        population = 0;
        memory = 0;
        culture = 0;
        trade = 0;
        cohesion = 0;
    } else {
        // 首次啟用，使用 YAML 定義的初始值並建立存檔
        save_settlement_state(id, runtime_data);
    }

    active_settlements[id] = runtime_data;
    return runtime_data;
}

// 儲存聚落動態變更
int save_settlement_state(string id, mapping data) {
    string save_path = sprintf("/data/state/settlements/%s", id);
    
    // 設定臨時變數以便 save_object 存檔
    population = data["population"];
    memory     = data["memory"];
    culture    = data["culture"];
    trade      = data["trade"];
    cohesion   = data["cohesion"];

    if (file_size("/data/state/settlements/") < 0) {
        mkdir("/data/state/settlements/");
    }

    int success = save_object(save_path);
    
    // 清空暫存，避免記憶體殘留
    population = 0;
    memory = 0;
    culture = 0;
    trade = 0;
    cohesion = 0;
    
    return success;
}

void create() {
    ::create();
    active_settlements = ([]);
    
    // 訂閱 FootprintGained 事件
    load_object("/secure/event_d.c")->subscribe("FootprintGained", "on_footprint");
}

// 根據踏印 ID 判定屬於哪一個聚落 (簡單對應)
string query_settlement_by_footprint(string fid) {
    if (strsrch(fid, "minxiong") != -1 || strsrch(fid, "打貓") != -1) {
        return "minxiong";
    }
    return 0;
}

// 查詢欄位
int query_memory(string id) {
    mapping s = load_settlement(id);
    return s ? s["memory"] : 0;
}

int query_culture(string id) {
    mapping s = load_settlement(id);
    return s ? s["culture"] : 0;
}

int query_population(string id) {
    mapping s = load_settlement(id);
    return s ? s["population"] : 0;
}

// 更新與累加屬性
void add_memory(string id, int val) {
    mapping s = load_settlement(id);
    if (!s) return;
    s["memory"] += val;
    save_settlement_state(id, s);
}

void add_culture(string id, int val) {
    mapping s = load_settlement(id);
    if (!s) return;
    s["culture"] += val;
    save_settlement_state(id, s);
}

void add_population(string id, int val) {
    mapping s = load_settlement(id);
    if (!s) return;
    s["population"] += val;
    save_settlement_state(id, s);
}

// 事件接收回呼
void on_footprint(mapping event) {
    mapping data = event["data"];
    string fid = data["footprint_id"];
    string pid = data["player_id"];
    
    string sid = query_settlement_by_footprint(fid);
    if (!sid) return;

    // 載入聚落，累加文化與記憶度
    mapping s = load_settlement(sid);
    if (!s) return;

    int old_mem = s["memory"];
    int old_cul = s["culture"];

    add_memory(sid, 5);
    add_culture(sid, 3);
    add_population(sid, 20);

    // 重新加載以取得最新值
    s = load_settlement(sid);

    object player = find_player(pid);
    if (player) {
        tell_object(player, sprintf(
            HIY "【聚落變鳴】你的探索回饋了「%s」聚落：\n"
            "  記憶值：%d ➡️ %d (+5)\n"
            "  文化值：%d ➡️ %d (+3)\n"
            "  人口數：%d ➡️ %d (+20)\n" NOR,
            s["name"], old_mem, s["memory"], old_cul, s["culture"], s["population"] - 20, s["population"]
        ));
    }

    // 發送聚落文明變動事件
    load_object("/secure/event_d.c")->publish("SettlementChanged", ([
        "settlement_id" : sid,
        "changes"       : ([ "memory": 5, "culture": 3, "population": 20 ])
    ]));

    // 同步回饋全服時代進度
    load_object("/daemon/timeline_d.c")->add_world_progress(5);
}
