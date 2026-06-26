# 源流福爾摩沙 MUDLib 開發藍圖

## 核心觀念

《源流福爾摩沙》不是傳統砍怪升級型 MUD。

傳統模式：

```text
打怪
→ 升級
→ 換裝
→ 更強怪
```

源流福爾摩沙：

```text
玩家
↓
踏印
↓
聚落
↓
文明
↓
歷史版本
```

玩家是文明建設者，而非征服者。

---

# 第一階段目標

不要先做：

- 戰鬥系統
- 技能系統
- 裝備系統
- NPC AI

先完成世界核心循環。

---

# 核心 Daemon

```text
/adm/daemons/

MEMORY_D.c
FOOTPRINT_D.c
SETTLEMENT_D.c
POPULATION_D.c
TIMELINE_D.c
FACTION_D.c
```

---

# 建議目錄架構

```text
/adm
/daemon
/world
/player
/npc
/cmds
```

---

# World Database

世界不應先從 room 開始。

應先從聚落資料開始。

範例：

```c
mapping location = ([
    "id":"minxiong",
    "name":"民雄",
    "level":"village",

    "population":1200,

    "industry":({
        "鳳梨",
        "糖業"
    }),

    "memory":35,

    "culture":42,

    "trade":18,
]);
```

---

# SETTLEMENT_D

查詢聚落狀態：

```c
SETTLEMENT_D->query_memory("minxiong");
```

增加聚落記憶：

```c
SETTLEMENT_D->add_memory(
    "minxiong",
    5
);
```

結果：

```text
民雄記憶值

35
↓
40
```

---

# 玩家資料結構

玩家沒有等級。

建議：

```c
mapping player_data = ([

    "footprints":([

    ]),

    "professions":([

    ]),

    "factions":({

    }),

    "villages":({

    }),

]);
```

避免：

```c
level
exp
hp
mp
```

---

# FOOTPRINT_D

新增踏印：

```c
FOOTPRINT_D->add_footprint(
    player,
    "打貓踏印"
);
```

取得後可直接回饋聚落：

```text
文化 +3
記憶 +5
```

---

# TIMELINE_D

世界版本為全服共用。

例如：

```c
current_version
```

```text
v0.2 海商紀
```

當文明度達標：

```c
SETTLEMENT_D->world_progress()
```

超過門檻後：

```c
TIMELINE_D->next_era();
```

世界公告：

```text
世界共振完成

即將進入：

v1.0 清領前期
```

---

# 第一個可玩版本（M1）

```text
M1
=====

✓ 玩家登入

✓ 民雄

✓ 踏印系統

✓ 聚落系統

✓ 記憶系統

✓ 版本系統
```

---

# 第一個遊戲循環

玩家輸入：

```text
look
```

顯示：

```text
民雄

記憶值：35
文化值：42
人口：1200

產業：
鳳梨
糖業
```

---

探索：

```text
explore old_station
```

獲得：

```text
糖鐵踏印
```

---

查詢聚落：

```text
village
```

顯示：

```text
民雄

記憶值
35 → 40

文化值
42 → 45
```

---

# 第二階段

完成 M1 後再開發：

```text
profession_system
npc_system
faction_system
historical_events
time_layer_instance
```

---

# 開發原則

永遠記住：

這不是一個以戰鬥為核心的 MUD。

這是一個以：

記憶 → 踏印 → 聚落 → 文明 → 時代

為核心循環的世界模擬型 MUD。

如果這條循環成立，
《源流福爾摩沙》就已經成功了一半。
