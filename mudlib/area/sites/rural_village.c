// /area/sites/rural_village.c
// 農村聚落

#include "/include/formosa.h"

inherit "/std/site.c";

void create() {
    site::create();

    set_entity_id("site:rural_village");
    set_entity_type("site");
    set_display_name("農村聚落");
    set_settlement_id("minxiong");
    set_era_id("modern");

    set_base_description(
        "這裡是由幾戶紅磚三合院組成的平靜聚落。\n"
        "埕前曬著剛收割的作物，幾隻家禽在泥地上低頭啄食，展現出純樸的鄉村風光。"
    );

    set_prop("travel_arrive_text", "你沿著田間小路，走進了這個炊煙裊裊的農村聚落。");
}
