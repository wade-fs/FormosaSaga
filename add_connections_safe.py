import os

file_path = "mudlib/data/yaml/settlements/minxiong.yaml"

# We will read the file and do string manipulation instead to preserve formatting
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

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

# Add reverse connections to map too
add_to_existing = {}
for k, vs in new_connections.items():
    for v in vs:
        if v not in add_to_existing:
            add_to_existing[v] = []
        add_to_existing[v].append(k)

# Process lines
out_lines = []
i = 0
in_map_data = False
current_site = None

while i < len(lines):
    line = lines[i]
    if line.startswith("map_data:"):
        in_map_data = True
    
    if in_map_data and line.startswith("  ") and not line.startswith("    "):
        current_site = line.strip().strip(":")
        
    out_lines.append(line)
    
    # Check if we just added connections for a site we want to append to
    if in_map_data and current_site in add_to_existing and "connections:" in line:
        for extra in add_to_existing[current_site]:
            out_lines.append(f"      - {extra}\n")
        del add_to_existing[current_site] # mark as done
        
    i += 1

# Append new nodes
for k, vs in new_connections.items():
    out_lines.append(f"  {k}:\n")
    out_lines.append(f"    connections:\n")
    for v in vs:
        out_lines.append(f"      - {v}\n")

with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(out_lines)

print("Connections added to minxiong.yaml via string manipulation.")
