// /area/sites/old_street.c
// 民雄老街

#include "/include/formosa.h"

inherit "/std/site.c";

void create() {
    site::create();

    set_entity_id("site:old_street");
    set_entity_type("site");
    set_display_name("民雄老街");
    set_settlement_id("minxiong");
    set_era_id("modern");

    set_base_description(
        "這裡曾是繁忙的商業街道，兩旁依然保留著幾棟巴洛克式的紅磚牌樓厝。\n"
        "騎樓下坐著泡茶聊天的老街鄰，店鋪裡傳出古老木門牙牙作響的聲音。"
    );

    set_prop("travel_arrive_text", "你漫步走進民雄老街，腳下是歷經風霜的石磚路。");
}
