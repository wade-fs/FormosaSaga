// /area/settlements/dashiye_temple.c
//
// 大士爺廟

#include "/include/formosa.h"

inherit "/std/site.c";

void create() {
    site::create();

    set_entity_id("site:dashiye_temple");
    set_entity_type("site");
    set_display_name("大士爺廟");
    set_settlement_id("minxiong");
    set_era_id("modern");

    set_base_description(
        "古老的廟宇石柱上雕刻著斑駁的神話神獸，香火的煙霧裊裊上升。\n"
        "信眾們在神前虔誠地投擲筊杯，祈求平安與豐收。"
    );

    set_prop("travel_arrive_text", "你走進大士爺廟的廟埕，空氣中瀰漫著濃郁的檀香與紙錢的微香。");
}
