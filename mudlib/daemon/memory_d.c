// /daemon/memory_d.c
// 
// 記憶守護進程，與 historical_event_d 配合，管理玩家對歷史記憶與事件的掌握狀態。

#include "/include/formosa.h"

inherit "/std/entity.c";

private nosave mapping player_memories; // ([ player_id: ({ memory_ids }) ])

void create() {
    entity::create();
    set_entity_id("daemon:memory");
    set_entity_type("daemon");
    player_memories = ([]);
}

int memory_completed(string memory_id) {
    // 預設將 v2.1 以後的歷史記憶完成條件做回傳判定，或提供對應 API。
    // 在此我們先回傳 1 以便測試，未來可接軌玩家存檔的記憶解鎖紀錄。
    return 1;
}

void on_fragment_accessible(object player, string mid) {
    if (!player || !mid) return;
    
    string pid = player->query_entity_id();
    if (!player_memories[pid]) player_memories[pid] = ({});
    
    if (member_array(mid, player_memories[pid]) == -1) {
        player_memories[pid] += ({ mid });
        tell_object(player, HIY "【記憶共鳴】你接觸到了歷史記憶片段：" HIG + mid + NOR "\n");
        
        emit("MemoryCompleted", ([
            "player_id": pid,
            "memory_id": mid,
            "settlement_id": "minxiong" // 預設給予 minxiong 做關聯
        ]));
    }
}
