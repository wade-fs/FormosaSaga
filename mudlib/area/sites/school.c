// /area/sites/school.c
// 民雄國小

#include "/include/formosa.h"

inherit "/std/site.c";

void create() {
    site::create();

    set_entity_id("site:school");
    set_entity_type("site");
    set_display_name("民雄國小");
    set_settlement_id("minxiong");
    set_era_id("modern");

    set_base_description(
        "校園裡傳來孩童朗朗的讀書聲與操場上的嬉鬧笑聲。\n"
        "校舍旁的幾棵老榕樹張開綠意盎然的樹冠，在陽光下灑下陰涼。"
    );

    set_prop("travel_arrive_text", "你穿過民雄國小的校門，踏入洋溢著朝氣的校園。");
}
