// /daemon/faction_d.c
#include "/include/ansi.h"

inherit "/std/object";

private nosave mapping loaded_factions;

void create() {
    ::create();
    loaded_factions = ([]);
}

// 載入勢力資料
mapping load_faction(string id) {
    if (!id || id == "") return 0;
    if (loaded_factions[id]) {
        return loaded_factions[id];
    }

    string yaml_path = sprintf("/world/factions/%s.yaml", id);
    if (file_size(yaml_path) <= 0) {
        return 0;
    }

    string content = read_file(yaml_path);
    if (!content) return 0;

    mapping data = yaml_decode(content);
    if (!data) return 0;

    loaded_factions[id] = data;
    return data;
}

int is_valid_faction(string id) {
    return load_faction(id) != 0;
}

string query_faction_name(string id) {
    mapping f = load_faction(id);
    return f ? f["name"] : 0;
}

string query_faction_type(string id) {
    mapping f = load_faction(id);
    return f ? f["type"] : 0;
}

string query_faction_base(string id) {
    mapping f = load_faction(id);
    return f ? f["base_location"] : 0;
}

string *query_faction_abilities(string id) {
    mapping f = load_faction(id);
    return f ? f["abilities"] : ({});
}

string *query_faction_skills(string id) {
    mapping f = load_faction(id);
    return f ? f["skills"] : ({});
}

string *query_faction_quests(string id) {
    mapping f = load_faction(id);
    return f ? f["quests"] : ({});
}
