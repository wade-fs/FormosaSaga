// /area/sites/ghost_house.c
// 民雄鬼屋 (劉家古樓)

#include "/include/formosa.h"

inherit "/std/site.c";

void create() {
    site::create();

    set_entity_id("site:ghost_house");
    set_entity_type("site");
    set_display_name("民雄鬼屋");
    set_settlement_id("minxiong");
    set_era_id("modern");

    set_base_description(
        "一棟荒廢的三層紅磚洋樓矗立在荒煙蔓草之中。\n"
        "巨大的榕樹氣根如蛛網般纏繞著斷垣殘壁，陽光穿過茂密的枝葉，灑落斑駁的光影。\n"
        "四周靜謐得有些詭異，隱約能聽到風吹過落葉的沙沙聲。"
    );

    set_prop("travel_arrive_text", "你沿著小徑走近那座傳說中的荒廢洋樓，四周的溫度似乎悄悄降了幾度。");
}

void player_enter(object player) {
    site::player_enter(player);
    if (player) {
        FOOTPRINT_D->add_footprint(player, "ghost_house_minxiong");
    }
}
