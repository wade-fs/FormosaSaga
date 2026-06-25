// /area/settlements/minxiong_old_station.c
//
// 民雄老車站

#include "/include/formosa.h"

inherit "/std/site.c";

void create() {
    site::create();

    set_entity_id("site:minxiong_old_station");
    set_entity_type("site");
    set_display_name("民雄車站");
    set_settlement_id("minxiong");
    set_era_id("modern");

    set_base_description(
        "木造的車站月台在熱氣中散發出乾木頭的氣味。\n"
        "鐵軌向南北兩端無限延伸，沒入遠處的熱浪與農田之中。"
    );

    set_prop("travel_arrive_text", "你走進了民雄車站，迎面而來的是月台的微風與甘蔗車的鳴笛聲。");
}

void player_enter(object player) {
    site::player_enter(player);
    if (player) {
        // 進入民雄老車站，授予糖鐵老車站聚落踏印
        FOOTPRINT_D->add_footprint(player, "sugar_railway_minxiong");
    }
}

