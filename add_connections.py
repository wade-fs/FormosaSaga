import yaml
import sys

file_path = "mudlib/data/yaml/settlements/minxiong.yaml"

with open(file_path, "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

new_connections = {
    "police_dormitory": ["minxiong_old_street"],
    "old_post_office": ["minxiong_old_street"],
    "credit_union": ["minxiong_old_street"],
    "farmers_association": ["minxiong_old_street"],
    "health_clinic": ["minxiong_old_street"],
    "public_hall": ["minxiong_old_street"],
    "library": ["minxiong_old_street"],

    "rice_shop": ["minxiong_market"],
    "photo_studio": ["minxiong_market"],
    "pharmacy": ["minxiong_market"],
    "grocery_store": ["minxiong_market"],
    "watch_shop": ["minxiong_market"],
    "shaved_ice_shop": ["minxiong_market"],
    "tailor_shop": ["minxiong_market"],
    "barbershop": ["minxiong_market"],
    "noodle_stand": ["minxiong_market"],
    "meat_stall": ["minxiong_market"],
    "fish_stall": ["minxiong_market"],
    "market_alley": ["minxiong_market"],

    "tea_house": ["minxiong_old_station"],
    "tavern": ["minxiong_old_station"],
    "cinema": ["minxiong_old_station"],

    "rice_mill": ["rural_village"],
    "lumber_yard": ["rural_village"],
    "blacksmith": ["rural_village"],
    "ancient_well": ["rural_village"],
    "earth_god_shrine": ["rural_village"],

    "ox_cart_road": ["outskirts"],
    "railway_side": ["outskirts"],

    "cemetery": ["ghost_house"],
    "bamboo_forest": ["ghost_house"],

    "pond": ["waterway"],
    "water_wheel": ["waterway"],

    "farmhouse": ["fengli_field"],
    "granary": ["fengli_field"],
    "tobacco_barn": ["fengli_field"]
}

# Add bidirectional connections
for site, connects in new_connections.items():
    if site not in data["map_data"]:
        data["map_data"][site] = {"connections": []}
    
    for conn in connects:
        if conn not in data["map_data"][site]["connections"]:
            data["map_data"][site]["connections"].append(conn)
            
        if conn in data["map_data"]:
            if site not in data["map_data"][conn]["connections"]:
                data["map_data"][conn]["connections"].append(site)

with open(file_path, "w", encoding="utf-8") as f:
    yaml.dump(data, f, allow_unicode=True, sort_keys=False)

print("Connections added to minxiong.yaml")
