// /testlib/cmds/admin/cmd_audit.c
// 統一管理員稽核指令 (Wizard Unified Audit Command)
// 支援：
//   audit settlement <ID>     (聚落地標與設定載入稽核)
//   audit errors              (查詢系統錯誤日誌)
//   audit status              (查詢當前 MUD 記憶體與執行狀態)

#include "/include/ansi.h"

inherit "/std/object";

int do_settlement_audit(object me, string id) {
    mapping result;
    string *sites;
    int i;

    write(HIY "正在對聚落 " + id + " 進行遊戲內稽核（P23.2 Settlement Audit）...\n" NOR);

    result = "/daemon/settlement_d"->load_settlement(id);
    if (!result) {
        write(RED "錯誤：找不到聚落「" + id + "」的設定檔或載入失敗。\n" NOR);
        return 1;
    }

    write("==================================================\n");
    write(" 聚落遊戲內稽核: " + result["name"] + " (" + id + ")\n");
    write("==================================================\n");

    sites = result["sites"];
    if (!pointerp(sites) || !sizeof(sites)) {
        write(RED "警告：該聚落沒有配置任何 Sites (地標)。\n" NOR);
    } else {
        write(HIC "地標清單與狀態查核：\n" NOR);
        for(i = 0; i < sizeof(sites); i++) {
            object site_obj = "/daemon/settlement_d"->get_site_object(sites[i]);
            if (!site_obj) {
                write(sprintf("  [%-25s] %s\n", sites[i], RED "● 載入失敗 (檔案不存在或語法錯誤)" NOR));
            } else {
                string name = site_obj->query_prop("canonical_name");
                if (!name) name = site_obj->query_prop("name");
                write(sprintf("  [%-25s] %s %s\n", sites[i], GRN "✓ 已載入" NOR, name ? ("(" + name + ")") : ""));
            }
        }
    }

    write("==================================================\n");
    write(GRN "聚落載入稽核完成。\n" NOR);
    return 1;
}

int do_errors_audit(object me) {
    string content;
    write(HIW "=== 最近系統錯誤日誌 (settlement_errors.log) ===\n" NOR);
    content = read_file("/log/settlement_errors.log");
    if (!content || content == "") {
        write(GRN "無任何錯誤記錄。\n" NOR);
    } else {
        write(content);
    }
    return 1;
}

int main(object me, string verb, string arg) {
    string cmd, subarg;

    if (me->query_role() != "god") {
        write("只有管理員可以使用此指令。\n");
        return 1;
    }

    if (!arg || arg == "") {
        write(HIW "語法指南 (audit <子指令> [參數])：\n" NOR
              "  audit settlement <聚落ID>  - 檢查聚落與所有地標是否能正常載入\n"
              "  audit errors               - 顯示最近的聚落載入錯誤日誌\n"
              "  audit status               - 顯示 MUD 核心系統狀態\n");
        return 1;
    }

    if (sscanf(arg, "%s %s", cmd, subarg) != 2) {
        cmd = arg;
        subarg = "";
    }

    cmd = trim(cmd);
    subarg = trim(subarg);

    switch (cmd) {
        case "settlement":
            if (subarg == "") {
                write("請指定聚落 ID。例如：audit settlement minxiong\n");
                return 1;
            }
            return do_settlement_audit(me, subarg);
        case "errors":
            return do_errors_audit(me);
        case "status":
            return "/cmds/admin/cmd_status"->main(me, "status", "");
        default:
            write("未知的稽核項目。請輸入 audit 取得說明。\n");
            return 1;
    }
}

string help() {
    return "【指令】\n  audit <項目>  管理員統一稽核工具，提供聚落載入、錯誤日誌與系統狀態一鍵檢查。\n";
}

string *query_verbs() {
    return ({ "audit" });
}

string query_category() {
    return "系統工具";
}
