// npc/slime.c - 史萊姆（新手怪）
inherit "/std/npc.c";

void create() {
    ::create();
    init_from_yaml("/world/npcs/slime.yaml");
}
