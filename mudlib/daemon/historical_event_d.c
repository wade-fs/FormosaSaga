// /daemon/historical_event_d.c
#include "/include/ansi.h"

inherit "/std/object";

private nosave mapping loaded_events;

void create() {
    ::create();
    loaded_events = ([]);
}

// 載入歷史事件資料
mapping load_event(string id) {
    if (!id || id == "") return 0;
    if (loaded_events[id]) {
        return loaded_events[id];
    }

    string yaml_path = sprintf("/world/events/%s.yaml", id);
    if (file_size(yaml_path) <= 0) {
        return 0;
    }

    string content = read_file(yaml_path);
    if (!content) return 0;

    mapping data = yaml_decode(content);
    if (!data) return 0;

    loaded_events[id] = data;
    return data;
}

int is_valid_event(string id) {
    return load_event(id) != 0;
}

string query_event_name(string id) {
    mapping e = load_event(id);
    return e ? e["name"] : 0;
}

string query_event_era(string id) {
    mapping e = load_event(id);
    return e ? e["era"] : 0;
}

string query_event_location(string id) {
    mapping e = load_event(id);
    return e ? e["location"] : 0;
}

string query_event_type(string id) {
    mapping e = load_event(id);
    return e ? e["type"] : 0;
}

string *query_event_npcs(string id) {
    mapping e = load_event(id);
    return e ? e["critical_npcs"] : ({});
}

string *query_event_flow(string id) {
    mapping e = load_event(id);
    return e ? e["player_flow"] : ({});
}

string *query_event_rewards(string id) {
    mapping e = load_event(id);
    return e ? e["rewards"] : ({});
}
