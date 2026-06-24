// /item/badge_newbie.c
inherit "/std/badge";

void create() {
    ::create();
    init_from_yaml("/world/items/badge_newbie.yaml");
}
