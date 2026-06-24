// /daemon/footprint_d.c
#include "/include/ansi.h"

inherit "/std/object";

void create() {
    ::create();
}

// 獲得踏印
void add_footprint(object player, string footprint_id) {
    if (!player || !userp(player) || !footprint_id || footprint_id == "") return;

    // 檢查玩家是否已經獲得過
    if (player->has_footprint_record(footprint_id)) {
        return; 
    }

    // 寫入玩家踏印紀錄
    player->add_footprint_record(footprint_id);

    // 傳送玩家通知
    tell_object(player, HIG "✨ 你獲得了踏印：『" + footprint_id + "』！\n" NOR);

    // 發布非同步踏印獲得事件
    load_object("/secure/event_d.c")->publish("FootprintGained", ([
        "player_id"    : player->get_id(),
        "footprint_id" : footprint_id,
        "timestamp"    : time()
    ]));
}
