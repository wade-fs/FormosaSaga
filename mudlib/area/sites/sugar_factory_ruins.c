// /area/sites/sugar_factory_ruins.c
// 民雄糖廠遺址

#include "/include/formosa.h"

inherit "/std/site.c";

void create() {
    site::create();

    set_entity_id("site:sugar_factory_ruins");
    set_entity_type("site");
    set_display_name("民雄糖廠遺址");
    set_settlement_id("minxiong");
    set_era_id("modern");

    set_base_description(
        "高聳的生鏽煙囪依然挺立在天空中，見證著那段製糖的黃金歲月。\n"
        "工廠內部的鐵軌早已鋪滿雜草，廢棄的廠房裡散落著損壞的舊機械零件。"
    );

    set_prop("travel_arrive_text", "你走進荒廢的製糖工廠，巨大的陰影籠罩下來。");
}
