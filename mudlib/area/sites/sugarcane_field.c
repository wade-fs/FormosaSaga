// /area/sites/sugarcane_field.c
// 甘蔗田

#include "/include/formosa.h"

inherit "/std/site.c";

void create() {
    site::create();

    set_entity_id("site:sugarcane_field");
    set_entity_type("site");
    set_display_name("甘蔗田");
    set_settlement_id("minxiong");
    set_era_id("modern");

    set_base_description(
        "一望無際的甘蔗林在風中搖曳，發出沙沙的聲響。\n"
        "長長的青翠綠葉向上伸展，遮蔽了視線，行走在田中彷彿置身於綠色的迷宮之中。"
    );

    set_prop("travel_arrive_text", "你撥開高聳的甘蔗葉，走進了茂密的甘蔗田中。");
}
