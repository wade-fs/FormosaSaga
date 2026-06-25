發現的問題
1. 文件與程式版本不同步

例如：

02_domain_model.md

定義：

World
Era
Site
Settlement
Memory
Footprint
Career
Faction

但是實作中：
```
world_d.c
❌ 不存在

site.c
⚠ 部分存在

career_d.c
❌ 不存在

resonance_d.c
❌ 不存在

oblivion_d.c
❌ 不存在
```

也就是：

文件是「目標架構」。

程式是「部分完成架構」。

2. 第一個遊戲循環尚未完成

README 已經明確寫出：
```
event_d
 ↓
settlement_d
 ↓
footprint_d
 ↓
world.c
 ↓
民雄老車站
 ↓
獲得踏印
 ↓
民雄記憶值 +5
```

# 但目前看起來：

- 已完成
	- Footprint

- 大部分完成
	- grant_footprint()
	- has_footprint()
	- Settlement


- 缺少
	- load_settlement()
	- save
	- event subscribe

- 這條鏈沒有完全落地。
```
Site
↓
Player進入
↓
FootprintGained
↓
Settlement記憶值變化
↓
Look可看見結果
```

3. Memory 與 Historical Event 尚未接軌

目前：

memory_d.c

還是測試版。

例如：
```
int memory_completed(string memory_id)
{
    return 1;
}
```
這顯然是 Stub。

但 Canon 裡面：
```
Memory
↓
Resonance
↓
Era Shift
```
是主線系統。

因此：

Memory 系統其實是最重要但尚未完成的部分。

我建議的下一步

不要再新增 Daemon。

不要再新增 Canon。

不要再寫更多世界觀。

# Milestone 3

- Memory Fragment 系統

    這才是整個作品的核心。

新增：

/world/memory/

例如：

id: minxiong_station_001

title: 嘉義線通車

era: qing_late

fragment:
  ...

玩家探索：

Site
↓
發現 Fragment
↓
MemoryCompleted
↓
Settlement + Memory

這會比打怪有趣得多，而且符合你的 Canon。

# Milestone 4
Era Progression

目前：

timeline_d.c

已經存在。

但尚未由世界事件驅動。

建議：
```
全島記憶度
↓
40%
↓
解鎖下一 Era
```

例如：
```
v0_1 荒野福爾摩沙

↓ 40%

v0_2 海商時代

↓ 60%

v1_0 乙未戰爭
```


優先順序

我會按照下面順序做：
```
P0
✓ 民雄垂直切片

P1
✓ Site Aggregate

P2
✓ Memory Fragment

P3
✓ Era Progression

P4
✓ Profession
✓ Faction

P5
✓ Specter
✓ Oblivion
✓ Resonance
```

因為你的核心循環還沒成立。

目前最有價值的工作，是把 README 裡那條：
```
走進民雄老車站
↓
獲得踏印
↓
民雄記憶值 +5
```
真正跑起來。

只要這條鏈完成，整個《源流福爾摩沙》的設計理念就首次被驗證了。
