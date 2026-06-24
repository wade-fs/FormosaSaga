// /cmds/admin/cmd_rehash.c
// 重新掃描並更新指令清單

#include "/include/config.h"
#include "/include/ansi.h"

inherit "/std/object";

int main(object me, string verb, string arg) {
    if (me->query_role() != "god" && me->query_role() != "wizard") {
        return 0;
    }

    object cmd_d = load_object("/secure/command_d");
    if (!cmd_d) {
        write("錯誤：找不到指令守護進程。\n");
        return 1;
    }

    int count = cmd_d->rehash();
    write("$HIW$指令系統重新掃描完成，共載入 " + count + " 個動詞。\n$NOR$");

    // 🚀 向所有在線玩家推送最新的 UI 指令清單
    object *us = users();
    object help_ob = load_object("/cmds/cmd_help");
    if (help_ob) {
        foreach (object u in us) {
            if (u && userp(u)) {
                help_ob->do_help_list(u, "");
                tell_object(u, "$HIG$【系統提示】指令系統已更新。\n$NOR$");
            }
        }
    }

    return 1;
}

string *query_verbs() { return ({ "rehash" }); }
string query_category() { return "Admin"; }

string help() {
    return "【管理指令】\n" +
           "  rehash    重新掃描 /cmds/ 目錄，並同步更新所有玩家的 UI 指令清單。\n";
}
