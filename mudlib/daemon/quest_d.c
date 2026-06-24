// /daemon/quest_d.c
// 任務守護進程 (Quest Daemon)

#include "/include/ansi.h"

inherit "/std/object";

mapping quest_list;

void create() {
    ::create();
    quest_list = ([
        "newbie_badge": ([
            "name": ([ "en": "Newbie Proof", "zh-TW": "新手證明", "zh-CN": "新手证明" ]),
            "desc": ([ "en": "Prove your courage to the Guild Master.", "zh-TW": "向公會會長證明你的勇氣。", "zh-CN": "向公会会长证明你的勇气。" ]),
            "level": 1,
            "reward": ([
                "exp": 100,
                "gold": 50,
                "badge": "/item/badge_newbie.c"
            ])
        ]),
        "wolf_hunter": ([
            "name": ([ "en": "Wolf Hunting", "zh-TW": "獵狼行動", "zh-CN": "猎狼行动" ]),
            "desc": ([ "en": "Eliminate 3 hungry wolves.", "zh-TW": "消滅 3 隻飢餓的野狼。", "zh-CN": "消灭 3 只饥饿的野狼。" ]),
            "level": 3,
            "goal": ([ "type": "kill", "target": "wolf", "count": 3 ]),
            "reward": ([
                "exp": 500,
                "gold": 200
            ])
        ]),
        "collect_fur": ([
            "name": ([ "en": "Fur Collection", "zh-TW": "毛皮需求", "zh-CN": "毛皮需求" ]),
            "desc": ([ "en": "Collect 3 wolf furs and give them to the armourer.", "zh-TW": "收集 3 張狼皮交給防具店老闆。", "zh-CN": "收集 3 张狼皮交给防具店老板。" ]),
            "level": 3,
            "goal": ([ "type": "item", "target": "狼皮", "count": 3 ]),
            "reward": ([
                "exp": 300,
                "gold": 150,
                "item": "/item/armour/leather_belt.c"
            ])
        ]),
        "slime_medicine": ([
            "name": ([ "en": "Medicine Ingredients", "zh-TW": "藥劑材料", "zh-CN": "药剂材料" ]),
            "desc": ([ "en": "Collect 5 globs of slime jelly and give them to the herbalist.", "zh-TW": "收集 5 團史萊姆黏液交給藥劑師。", "zh-CN": "收集 5 团史莱姆黏液交给药剂师。" ]),
            "level": 1,
            "goal": ([ "type": "item", "target": "史萊姆黏液", "count": 5 ]),
            "reward": ([
                "exp": 200,
                "gold": 80
            ])
        ]),
        "crab_armour": ([
            "name": ([ "en": "Crab Armour", "zh-TW": "加固甲殼", "zh-CN": "加固甲壳" ]),
            "desc": ([ "en": "Collect 2 crab shells and give them to the blacksmith.", "zh-TW": "收集 2 塊螃蟹殼交給鐵匠。", "zh-CN": "收集 2 块螃蟹壳交给铁匠。" ]),
            "level": 2,
            "goal": ([ "type": "item", "target": "螃蟹殼", "count": 2 ]),
            "reward": ([
                "exp": 250,
                "gold": 100
            ])
        ])
    ]);
}

mapping query_quest_info(string qid) {
    return quest_list[qid];
}

int accept_quest(object me, string qid) {
    mapping info = query_quest_info(qid);
    if (!info) return 0;

    if (me->query_level() < info["level"]) {
        write(to_string(_t("level_low_err")) + "\n");
        return 0;
    }

    if (me->query_quest(qid)) {
        write(to_string(_t("quest_already_accepted")) + "\n");
        return 0;
    }

    me->set_quest(qid, ([
        "status": "active",
        "start_time": time(),
        "progress": ([ "count": 0 ])
    ]));
    
    string accept_msg = to_string(_t("quest_accept"));
    accept_msg = replace_string(accept_msg, "$quest", to_string(select_lang(info["name"])));
    write("$HIG$" + accept_msg + "$NOR$" + "\n");
    
    string desc_msg = to_string(_t("quest_desc"));
    desc_msg = replace_string(desc_msg, "$desc", to_string(select_lang(info["desc"])));
    write(desc_msg + "\n");
    
    me->save();
    return 1;
}

int complete_quest(object me, string qid) {
    mapping qdata = me->query_quest(qid);
    if (!qdata || qdata["status"] != "active") return 0;

    mapping info = query_quest_info(qid);
    
    // 🚀 如果是蒐集任務，檢查並扣除物品
    if (info["goal"] && info["goal"]["type"] == "item") {
        string target_name = info["goal"]["target"];
        int req_count = info["goal"]["count"];
        
        object *inv = all_inventory(me);
        object *found = ({});
        foreach (object ob in inv) {
            if (ob->query_name() == target_name) found += ({ ob });
        }
        
        if (sizeof(found) < req_count) {
            string err = to_string(_t("quest_item_missing"));
            err = replace_string(err, "$item", to_string(target_name));
            err = replace_string(err, "$got", sprintf("%d", sizeof(found)));
            err = replace_string(err, "$req", sprintf("%d", req_count));
            write(err + "\n");
            return 0;
        }
        
        // 扣除物品
        for (int i = 0; i < req_count; i++) {
            destruct(found[i]);
        }
        string give_msg = to_string(_t("quest_item_give"));
        give_msg = replace_string(give_msg, "$count", sprintf("%d", req_count));
        give_msg = replace_string(give_msg, "$item", to_string(target_name));
        write(give_msg + "\n");
    }

    // 給予獎勵
    mapping reward = info["reward"];
    if (reward["exp"]) me->gain_exp(reward["exp"]);
    if (reward["gold"]) me->gain_gold(reward["gold"]);
    
    // 🚀 新增：公會貢獻獎勵
    if (me->query_guild()) {
        int gexp = reward["exp"] / 5; // 預設貢獻度為經驗值的 20%
        if (gexp < 1) gexp = 1;
        me->add_guild_exp(gexp);
        tell_object(me, "$HIG$" + sprintf("%s%d\n", to_string(_t("guild_exp_gain")), gexp) + "$NOR$");
    }

    if (reward["badge"]) {
        object badge = clone_object(reward["badge"]);
        if (badge) {
            string msg = to_string(_t("quest_reward_get"));
            if (msg == "quest_reward_get") msg = "你獲得了 $item！";
            msg = replace_string(msg, "$item", to_string(badge->query_short()));
            write(msg + "\n");
            move_object(badge, me);
        }
    }
    if (reward["item"]) {
        object ob = clone_object(reward["item"]);
        if (ob) {
            string msg = to_string(_t("quest_reward_item"));
            if (msg == "quest_reward_item") msg = "你獲得了獎勵物品：$item！";
            msg = replace_string(msg, "$item", to_string(ob->query_short()));
            write(msg + "\n");
            if (!move_object(ob, me)) move_object(ob, environment(me));
        }
    }

    qdata["status"] = "completed";
    qdata["end_time"] = time();
    me->set_quest(qid, qdata);
    
    string complete_msg = to_string(_t("quest_complete"));
    complete_msg = replace_string(complete_msg, "$quest", to_string(select_lang(info["name"])));
    write("$HIY$" + complete_msg + "$NOR$" + "\n");
    
    me->save();
    return 1;
}

// 🚀 新增：檢查殺怪進度
void check_kill_progress(object me, string monster_file) {
    mapping quests = me->query_quests();
    if (!quests) return;

    mixed ks = keys(quests);
    foreach (string qid in ks) {
        mapping qdata = quests[qid];
        if (qdata["status"] != "active") continue;

        mapping info = quest_list[qid];
        if (!info["goal"] || info["goal"]["type"] != "kill") continue;

        // 檢查是否為目標怪物 (支援 partial path 匹配)
        if (strsrch(monster_file, info["goal"]["target"]) != -1) {
            int current = qdata["progress"]["count"] + 1;
            int total = info["goal"]["count"];
            
            me->update_quest_progress(qid, "count", current);
            string progress_msg = to_string(_t("quest_progress"));
            if (progress_msg == "quest_progress") progress_msg = "$HIG$【任務進度】$NOR$" + "$quest：$current / $total";
            progress_msg = replace_string(progress_msg, "$quest", to_string(select_lang(info["name"])));
            progress_msg = replace_string(progress_msg, "$current", sprintf("%d", current));
            progress_msg = replace_string(progress_msg, "$total", sprintf("%d", total));
            tell_object(me, progress_msg + "\n");

            if (current >= total) {
                tell_object(me, "$HIY$" + to_string(_t("quest_goal_met")) + "\n$NOR$");
            }
        }
    }
}

mapping query_all_quests() {
    return quest_list;
}
