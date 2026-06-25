// /area/sites/waterway.c
// 灌溉水圳

#include "/include/formosa.h"

inherit "/std/site.c";

void create() {
    site::create();

    set_entity_id("site:waterway");
    set_entity_type("site");
    set_display_name("灌溉水圳");
    set_settlement_id("minxiong");
    set_era_id("modern");

    set_base_description(
        "清澈的水流在水泥砌成的渠道中淙淙流過，灌溉著兩旁的農田。\n"
        "圳溝旁有幾株野生的野薑花，散發出淡淡的清香。"
    );

    set_prop("travel_arrive_text", "你沿著圳溝旁的小路前行，耳邊傳來潺潺的水流聲。");
}
