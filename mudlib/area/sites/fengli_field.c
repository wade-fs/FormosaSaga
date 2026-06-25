// /area/sites/fengli_field.c
// 鳳梨田

#include "/include/formosa.h"

inherit "/std/site.c";

void create() {
    site::create();

    set_entity_id("site:fengli_field");
    set_entity_type("site");
    set_display_name("鳳梨田");
    set_settlement_id("minxiong");
    set_era_id("modern");

    set_base_description(
        "整齊排列的鳳梨植株覆蓋在黃土丘陵上，在烈日下散發出微酸的熱氣。\n"
        "果實頂端戴著遮陽的紙帽，在陽光下十分引人注目。"
    );

    set_prop("travel_arrive_text", "你走上平緩的紅土小丘，四周是一整片遼闊的鳳梨田。");
}
