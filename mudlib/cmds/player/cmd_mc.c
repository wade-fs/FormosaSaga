// /cmds/cmd_mc.c  ── Light Minecraft 互動指令 ────────────────
// 負責在世界內的操作：move / dig / place / map / pos / inv / help
// 觸發詞：mc
// 需在 /area/lm/world.c 環境中才能執行大部分子指令

#include "/include/config.h"
#include "/include/ansi.h"

inherit "/std/object.c";

int in_lm(object me) {
    object env = environment(me);
    return (env && env->query_is_lm_world());
}

int main(object me, string verb, string arg) {

    // 🚀 核心修正：統一攔截離開指令 (改為 back)
    if (in_lm(me)) {
        if (verb == "back" || (verb == "go" && arg == "back")) {
            arg = "leave";
        }
    } else if (verb == "back" || verb == "go") {
        // 不在創界內，回退給系統處理
        return 0;
    }

    if (!arg || arg == "") arg = "help";
    string *parts = explode(trim(lower_case(arg)), " ");
    string sub = parts[0];

    // ── mc help ─────────────────────────────────────────────
    if (sub == "help") {
        write(
            "$HIW$\n═══ Light Minecraft 指令 ═══\n$NOR$" +
            "  " + "$CYN$mc map$NOR$" +                    "                重新整理地圖視窗\n" +
            "  " + "$CYN$mc move n|s|e|w$NOR$" +           "        移動（可用 WASD 快速鍵）\n" +
            "  " + "$CYN$mc dig <x> <y>$NOR$" +            "         挖掘指定座標方塊\n" +
            "  " + "$CYN$mc place <x> <y> <類型>$NOR$" +   " 放置方塊\n" +
            "  " + "$CYN$mc pos$NOR$" +                    "                顯示目前座標\n" +
            "  " + "$CYN$mc inv$NOR$" +                    "                列出背包方塊\n" +
            "  " + "$CYN$mc give <類型> <數量>$NOR$" +      "   給自己方塊（測試用）\n" +
            "  " + "$CYN$mc back$NOR$" +                   "               離開創界 (回到原處)\n" +
            "\n方塊類型：grass dirt stone log planks leaves sand coal iron gold brick\n\n"
        );
        return 1;
    }

    // ── mc leave（不需在世界裡，改稱為 back）───────────────────────────
    if (sub == "leave" || sub == "back") {
        // 🚀 關鍵同步：第一時間通知前端關閉 MC 介面
        tell_object(me, "{\"ui\": \"mc_exit\"}\n");

        if (in_lm(me)) {
            environment(me)->player_leave(me);
        }

        // 🚀 核心優化：嘗試回到進入前的房間
        string return_path = me->query_temp("lm_return_room");
        object dest;
        
        if (return_path && strsrch(return_path, "/std/") == -1) {
            dest = load_object(return_path);
            me->delete_temp("lm_return_room");
        }
        
        // 備援：若無紀錄則回到預設新手村
        if (!dest) {
            dest = load_object(START_ROOM);
        }

        if (dest) {
            // 🚀 關鍵同步：通知前端關閉 MC 介面
            tell_object(me, "{\"ui\": \"mc_exit\"}\n");
            
            me->move(dest);
            me->save(); // 🚀 修正：離開創界後立即存檔，避免 last_location 殘留
            dest->look_room(me);
        } else {
            write("$RED$找不到目的地。\n$NOR$");
        }
        return 1;
    }

    // ── 以下需在創界內 ──────────────────────────────────────
    if (!in_lm(me)) {
        write("$YEL$你必須在創界中才能使用此指令。\n$NOR$");
        return 1;
    }

    object world = environment(me);

    // ── mc build ──────────────────────────────────────────────
    if (sub == "build") {
        string role = me->query_role();
        if (role != "god" && role != "wizard") {
            write("$RED$你沒有此指令的權限。\n$NOR$"); return 1;
        }
        if (sizeof(parts) < 2) {
            write("用法：mc build <檔案路徑>\n"); return 1;
        }
        string file = parts[1];
        if (file[0..0] != "/") file = "/" + file;
        
        string content = read_file(file);
        if (!content || content == "") {
            write("$RED$無法讀取檔案或檔案為空。\n$NOR$"); return 1;
        }
        
        int *pos = world->query_player_pos(me);
        if (!pos) pos = ({ SPAWN_X, SPAWN_Y });
        
        world->import_map(content, pos[0], pos[1]);
        write("$RED$地圖建構完成！\n$NOR$");
        return 1;
    }

    // ── mc import ─────────────────────────────────────────────
    if (sub == "import") {
        string role = me->query_role();
        if (role != "god" && role != "wizard") {
            write("$RED$你沒有此指令的權限。\n$NOR$"); return 1;
        }
        if (sizeof(parts) < 2) {
            write("用法：mc import <資料>\n"); return 1;
        }
        string data = arg[7..]; // 移除 "import "
        // 把 \n 轉換為真正的換行，因為從網頁傳來可能會變成單行或 JSON 編碼
        data = replace_string(data, "\\n", "\n");

        int *pos = world->query_player_pos(me);
        if (!pos) pos = ({ SPAWN_X, SPAWN_Y });
        
        world->import_map(data, pos[0], pos[1]);
        write("$RED$地圖導入完成！\n$NOR$");
        return 1;
    }

    // ── mc map ──────────────────────────────────────────────
    if (sub == "map") {
        world->broadcast_map(me);
        return 1;
    }

    // ── mc pos ──────────────────────────────────────────────
    if (sub == "pos") {
        int *pos = world->query_player_pos(me);
        if (!pos) {
            write("座標未知，請輸入 mc map 重新同步。\n");
        } else {
            write(sprintf("你目前在座標 " + "$CYN$(%d, %d)$NOR$" + "。\n",
                pos[0], pos[1]));
        }
        return 1;
    }

    // ── mc inv ──────────────────────────────────────────────
    if (sub == "inv") {
        object *items = filter(all_inventory(me),
            (: objectp($1) && strsrch(base_name($1), "/area/lm/block_item") == 0 :));
        if (!sizeof(items)) {
            write("背包中沒有任何方塊。\n");
            return 1;
        }
        mapping counts = ([]);
        foreach (object it in items) {
            string t = it->query_block_type();
            m_add(counts, t, (counts[t] ? counts[t] : 0) + 1);
        }
        write("$CYN$【方塊背包】\n$NOR$");
        foreach (string t in sort_array(keys(counts), 1)) {
            write(sprintf("  %-10s x%d\n", t, counts[t]));
        }
        return 1;
    }

    // ── mc move ─────────────────────────────────────────────
    if (sub == "move") {
        if (sizeof(parts) < 2) {
            write("用法：mc move n|s|e|w\n"); return 1;
        }
        int dx = 0, dy = 0;
        // n = 畫面上方 = y+1；s = 畫面下方 = y-1
        switch(parts[1]) {
            case "n": case "north": case "up":    dy =  1; break;
            case "s": case "south": case "down":  dy = -1; break;
            case "e": case "east":  case "right": dx =  1; break;
            case "w": case "west":  case "left":  dx = -1; break;
            default:
                write("方向請輸入 n/s/e/w\n"); return 1;
        }
        int r = world->move_player(me, dx, dy);
        if (r == 1) write("已到達世界邊界。\n");
        else if (r == 2) write("前方有方塊擋路！試試 " + "$CYN$mc dig$NOR$" + " 挖掘。\n");
        return 1;
    }

    // ── mc dig ──────────────────────────────────────────────
    if (sub == "dig") {
        if (sizeof(parts) < 3) {
            write("用法：mc dig <x> <y>\n"); return 1;
        }
        int x = to_int(parts[1]);
        int y = to_int(parts[2]);
        int r = world->dig_block(me, x, y);
        switch(r) {
            case 0: write("$RED$挖掘成功！方塊已加入背包。\n$NOR$"); break;
            case 1: write("$RED$座標超出世界範圍（0~59, 0~39）。\n$NOR$"); break;
            case 2: write("$YEL$那個位置沒有方塊。\n$NOR$"); break;
            case 3: write("$YEL$水不能挖掘。\n$NOR$"); break;
        }
        return 1;
    }

    // ── mc place ────────────────────────────────────────────
    if (sub == "place") {
        if (sizeof(parts) < 4) {
            write("用法：mc place <x> <y> <類型>\n"); return 1;
        }
        int x = to_int(parts[1]);
        int y = to_int(parts[2]);
        string btype = parts[3];
        int r = world->place_block(me, x, y, btype);
        switch(r) {
            case 0: write("$RED$放置成功！\n$NOR$"); break;
            case 1: write("$RED$座標超出世界範圍。\n$NOR$"); break;
            case 2: write("$YEL$那個位置已有方塊。\n$NOR$"); break;
            case 3: write("$YEL$背包裡沒有 " + btype + " 方塊。先用 mc dig 取得。\n$NOR$"); break;
        }
        return 1;
    }

    // ── mc give（測試/管理指令）─────────────────────────────
    if (sub == "give") {
        string role = me->query_role();
        if (role != "god" && role != "wizard") {
            write("$RED$你沒有此指令的權限。\n$NOR$"); return 1;
        }
        if (sizeof(parts) < 2) {
            write("用法：mc give <類型> [數量]\n"); return 1;
        }
        string btype = parts[1];
        int amount = (sizeof(parts) >= 3) ? to_int(parts[2]) : 1;
        if (amount < 1) amount = 1;
        if (amount > 64) amount = 64;

        int i;
        for (i = 0; i < amount; i++) {
            object item = clone_object("/area/lm/block_item");
            if (item) {
                item->set_block_type(btype);
                move_object(item, me);
            }
        }
        write("$RED$" + sprintf("給予 %s x%d。\n", btype, amount) + "$NOR$");
        return 1;
    }

    write("未知子指令。輸入 " + "$CYN$mc help$NOR$" + " 查看說明。\n");
    return 1;
}

string *query_verbs() { return ({ "mc" }); }

string query_category() {
    return select_lang(([ "en": "World", "zh-TW": "創界", "zh-CN": "创界" ]));
}

string help() {
    return "【mc 創界指令】\n" +
           "  mc map              開啟 2D 地圖視窗\n" +
           "  mc move n|s|e|w     在世界中移動（WASD 快速鍵）\n" +
           "  mc dig <x> <y>      挖掘指定位置方塊\n" +
           "  mc place <x> <y> <類型>  放置方塊\n" +
           "  mc pos              顯示目前座標\n" +
           "  mc inv              列出背包方塊\n" +
           "  mc give <類型> [數]  給予方塊（god/wizard）\n" +
           "  mc build <檔案>     從伺服器檔案匯入地圖\n" +
           "  mc import <資料>    直接匯入地圖文字\n" +
           "  mc back             離開創界 (回到進入前房間)\n";
}
