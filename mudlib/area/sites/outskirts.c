// /area/sites/outskirts.c
// 民雄郊區

#include "/include/formosa.h"

inherit "/std/site.c";

void create() {
    site::create();

    set_entity_id("site:outskirts");
    set_entity_type("site");
    set_display_name("民雄郊區");
    set_settlement_id("minxiong");
    set_era_id("modern");

    set_base_description(
        "這裡逐漸遠離了聚落中心，視野隨之開闊。\n"
        "小路兩旁散落著零星的房舍與灌木叢，微風中帶著泥土的芳香與青草的氣息。"
    );

    set_prop("travel_arrive_text", "你沿著漫長的小路向外走去，來到了民雄平靜的郊區。");
}
