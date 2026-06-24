// npc/wolf.c - 野狼（中階怪）
inherit "/std/npc.c";

void create() {
    ::create();
    init_from_yaml("/world/npcs/wolf.yaml");
}
