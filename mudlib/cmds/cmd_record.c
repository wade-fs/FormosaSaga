// /cmds/cmd_record.c
// 文人專屬指令：記錄/考據

inherit "/std/object";

#include "/include/ansi.h"

int main(object me, string verb, string arg) {
    if (me->query("career") != "scholar") {
        write(select_lang(([ "zh-TW": "你並非文人，不懂得如何進行考據與記錄。\n", "en": "You are not a scholar and do not know how to record history.\n" ])));
        return 1;
    }

    object here = environment(me);
    string settlement = here ? here->query_settlement_id() : "";

    string msg;
    int exp_gain = 10;
    
    // 嘉義與鹿港等文化發源地給予加成
    if (settlement == "chiayi" || settlement == "lukang") {
        msg = "在這裡，豐富的文史底蘊讓你文思泉湧，你提筆記錄下珍貴的口述歷史與風土民情。";
        exp_gain = 25;
    } else {
        msg = "你仔細觀察周遭的環境與碑文，試圖從蛛絲馬跡中考據出被遺忘的歷史碎片。";
        exp_gain = 12;
    }

    write("$HMAG$" + msg + "$NOR$\n");
    say(me->query_name() + " 拿出手札，認真地記錄著周遭的文史細節。\n");

    me->add_exp(exp_gain);
    write("你獲得了 " + exp_gain + " 點經驗值與文人修練點。\n");

    object career_d = find_object("/daemon/career_d.c");
    if (career_d) {
        career_d->add_points(me, "scholar", 3); // 文人記錄固定增加較多修練點
    }

    // 機率性給予記憶或勢力聲望 (示意)
    if (random(100) < 20) {
        write("$HIY$你在考據的過程中，似乎觸及了某個古老陣營的秘辛...\n$NOR$");
    }

    return 1;
}

string help() {
    return select_lang(([
        "zh-TW": "【指令】\n  record    (文人專屬) 記錄文史與考據，在特定文化發源地(如嘉義)有額外加成。\n",
        "en": "【Command】\n  record    (Scholar only) Record history. Bonus in cultural hubs.\n"
    ]));
}

string *query_verbs() {
    return ({ "record", "research" });
}

string query_category() {
    return "職涯";
}
