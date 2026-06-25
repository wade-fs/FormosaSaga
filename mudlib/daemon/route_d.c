// /daemon/route_d.c
//
// 路線與通道管理服務。
//
// 職責：
//   - 載入與索引所有 data/yaml/routes/ 下的路線定義（包含聯外交通與聯內通道）
//   - 提供旅行耗時與鄰近通路的動態查詢。

#include "/include/formosa.h"

inherit "/std/entity.c";

private nosave mapping route_cache;  // ([ route_id: route_data ])
private nosave mapping names_cache; // ([ route_id: ([ era_id: name ]) ])

void scan_dir(string dir) {
    string *files = get_dir(dir);
    if (!files) return;

    foreach (string file in files) {
        if (file == "." || file == "..") continue;
        string path = dir + file;
        int sz = file_size(path);
        if (sz == -2) {
            // 目錄，遞迴掃描
            scan_dir(path + "/");
        } else if (strlen(file) >= 5 && substr(file, strlen(file)-5, 5) == ".yaml") {
            string content = read_file(path);
            if (!content) continue;
            mapping data = yaml_decode(content);
            if (!data || !data["id"]) continue;

            string id = data["id"];
            route_cache[id] = data;

            // 快取多語系/多時代名稱
            mapping n_map = ([]);
            if (pointerp(data["names"])) {
                foreach (mapping name_entry in data["names"]) {
                    if (name_entry["era"] && name_entry["name"]) {
                        n_map[name_entry["era"]] = name_entry["name"];
                    }
                }
            }
            names_cache[id] = n_map;
        }
    }
}

void rehash() {
    route_cache = ([]);
    names_cache = ([]);
    scan_dir("/data/yaml/routes/");
}

void create() {
    ::create();
    set_entity_id("daemon:route");
    set_entity_type("daemon");
    rehash();
}

mapping load_route(string route_id) {
    if (!route_cache) rehash();
    return route_cache[route_id];
}

mapping query_names_mapping(string route_id) {
    if (!names_cache) rehash();
    return names_cache[route_id];
}

string query_travel_time(string from, string to, string transport_type) {
    if (!route_cache) rehash();
    
    foreach (string id, mapping r in route_cache) {
        mixed nodes = r["nodes"];
        if (pointerp(nodes) && member_array(from, nodes) != -1 && member_array(to, nodes) != -1) {
            mixed tt = r["travel_time"];
            if (mapp(tt)) {
                if (transport_type && tt[transport_type]) return tt[transport_type];
                mixed ks = keys(tt);
                if (sizeof(ks) > 0) return tt[ks[0]];
            } else if (stringp(tt)) {
                return tt;
            }
        }
    }
    return 0;
}

string *query_connections(string site_id) {
    if (!route_cache) rehash();
    string *conn = ({});
    foreach (string id, mapping r in route_cache) {
        mixed nodes = r["nodes"];
        if (pointerp(nodes) && member_array(site_id, nodes) != -1) {
            foreach (string node in nodes) {
                if (node != site_id && member_array(node, conn) == -1) {
                    conn += ({ node });
                }
            }
        }
    }
    return conn;
}
