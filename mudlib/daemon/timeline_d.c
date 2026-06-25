// /daemon/timeline_d.c
#include "/include/ansi.h"

inherit "/std/object";

string current_era_id;
int world_progress;

void save_state() {
    if (file_size("/data/state/system/") < 0) {
        mkdir("/data/state/system/");
    }
    save_object("/data/state/system/timeline");
}

void restore_state() {
    if (file_size("/data/state/system/timeline.o") > 0) {
        restore_object("/data/state/system/timeline");
    } else {
        current_era_id = "v0_1";
        world_progress = 0;
        save_state();
    }
    // 兼容舊存檔遷移
    if (current_era_id == "v0.1_wild_era") {
        current_era_id = "v0_1";
        save_state();
    } else if (current_era_id == "v0.2_sea_merchants") {
        current_era_id = "v0_2";
        save_state();
    }
}

void create() {
    ::create();
    restore_state();
}

string query_current_era() {
    return current_era_id;
}

int query_world_progress() {
    return world_progress;
}

// 取得當前時代的詳細資料 (從 YAML 讀取)
mapping query_current_era_data() {
    string yaml_path = sprintf("/world/eras/%s.yaml", current_era_id);
    if (file_size(yaml_path) <= 0) return 0;
    string content = read_file(yaml_path);
    if (!content) return 0;
    return yaml_decode(content);
}

// 驗證是否滿足推展至下一時代的條件
int validate_next_era_transition() {
    string next_era_id;
    if (current_era_id == "v0_1") {
        next_era_id = "v0_2";
    } else if (current_era_id == "v0_2") {
        next_era_id = "v1_0";
    } else {
        return 0; // 已是最高時代
    }

    // 檢查目標時代的 YAML 設定檔是否存在且格式正確
    string yaml_path = sprintf("/world/eras/%s.yaml", next_era_id);
    if (file_size(yaml_path) <= 0) {
        log_file("validation_errors.log", sprintf("時代推展失敗: 找不到目標時代的設定檔 '%s'\n", yaml_path));
        return 0;
    }

    string content = read_file(yaml_path);
    mapping era_data = yaml_decode(content);
    if (!era_data || !mapp(era_data)) {
        log_file("validation_errors.log", sprintf("時代推展失敗: 無法解析時代設定檔 '%s'\n", yaml_path));
        return 0;
    }

    if (!stringp(era_data["id"]) || !stringp(era_data["name"])) {
        log_file("validation_errors.log", sprintf("時代推展失敗: 設定檔 '%s' 缺少 id 或 name\n", yaml_path));
        return 0;
    }

    return 1;
}

// 時代推進
void next_era() {
    if (!validate_next_era_transition()) {
        write("【系統提示】目前世界不符合進入下一時代的驗證條件，取消時代推展。\n");
        return;
    }

    string old_era = current_era_id;
    if (current_era_id == "v0_1") {
        current_era_id = "v0_2";
    } else if (current_era_id == "v0_2") {
        current_era_id = "v1_0";
    } else {
        return; // 已是最高時代
    }

    world_progress = 0; // 重設進度
    save_state();

    // 讀取新時代的名稱
    mapping era_data = query_current_era_data();
    string name = era_data ? era_data["name"] : current_era_id;

    // 廣播給所有線上玩家
    shout(HIW "\n【世界共振完成】\n即將進入時代版本：" HIG + name + " (" + current_era_id + ")" + NOR "\n\n");
    
    // 發送領域事件
    load_object("/secure/event_d.c")->publish("EraShifted", ([
        "from_era"  : old_era,
        "to_era"    : current_era_id,
        "timestamp" : time()
    ]));
}

// 增加世界文明進度
void add_world_progress(int val) {
    world_progress += val;
    save_state();

    // 如果進度達標 (例如 100)，自動推展時代
    if (world_progress >= 100) {
        next_era();
    }
}
