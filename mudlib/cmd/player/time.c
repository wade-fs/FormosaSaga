// /cmd/time.c
// 查詢目前遊戲時間與 NPC 日程狀態

#include "/include/formosa.h"

int main(object me, string args) {
    string game_time = SCHEDULE_D->query_game_time();
    int minutes = SCHEDULE_D->query_game_time_minutes();
    int hh = minutes / 60;
    
    string period;
    if (hh >= 5 && hh < 8)    period = "清晨";
    else if (hh >= 8 && hh < 12)  period = "上午";
    else if (hh >= 12 && hh < 14) period = "正午";
    else if (hh >= 14 && hh < 18) period = "下午";
    else if (hh >= 18 && hh < 21) period = "傍晚";
    else                           period = "夜晚";
    
    tell_object(me, "╔══════════════════╗\n");
    tell_object(me, sprintf("  現在是 %s  %s\n", period, game_time));
    tell_object(me, "╚══════════════════╝\n");
    tell_object(me, "（遊戲時間每 15 秒推進 15 分鐘）\n");
    
    // 顯示場景內 NPC 動態
    object env = environment(me);
    if (!env) return 1;
    
    string npc_status = "";
    object *inv = all_inventory(env);
    foreach (object ob in inv) {
        if (!ob->is_npc()) continue;
        string act = ob->query_action_msg();
        if (act && act != "") {
            npc_status += "  " + ob->query_short() + "：" + act + "\n";
        }
    }
    
    if (npc_status != "") {
        tell_object(me, "\n【場景動態】\n" + npc_status);
    }
    
    return 1;
}
