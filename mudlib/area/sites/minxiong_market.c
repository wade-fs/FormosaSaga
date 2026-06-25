// /area/settlements/minxiong_market.c
//
// 民雄市場

#include "/include/formosa.h"

inherit "/std/site.c";

void create() {
    site::create();

    set_entity_id("site:minxiong_market");
    set_entity_type("site");
    set_display_name("民雄市場");
    set_settlement_id("minxiong");
    set_era_id("modern");

    set_base_description(
        "這裡聚集了許多小攤販，菜葉與熟食的氣味交織在空氣中。\n"
        "農人們挑著扁擔，高聲談論著今年的鳳梨收成。"
    );

    set_prop("travel_arrive_text", "你穿過熙熙攘攘的人群，來到了民雄熱鬧的市集。");
}
