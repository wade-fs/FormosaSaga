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

也就是：

文件是「目標架構」。

程式是「部分完成架構」。

2. 第一個遊戲循環尚未完成

README 已經明確寫出：

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

但目前看起來：

Footprint

已完成

grant_footprint()
has_footprint()
Settlement

大部分完成

load_settlement()
save
event subscribe
缺少
Site
↓
Player進入
↓
FootprintGained
↓
Settlement記憶值變化
↓
Look可看見結果

這條鏈沒有完全落地。

3. Memory 與 Historical Event 尚未接軌

目前：

memory_d.c

還是測試版。

例如：

int memory_completed(string memory_id)
{
    return 1;
}

這顯然是 Stub。

但 Canon 裡面：

Memory
↓
Resonance
↓
Era Shift

是主線系統。

因此：

Memory 系統其實是最重要但尚未完成的部分。

我建議的下一步

不要再新增 Daemon。

不要再新增 Canon。

不要再寫更多世界觀。

先完成：

Milestone 1
民雄垂直切片

目標：

讓玩家可以完成第一個踏印。

Step 1

建立：

/area/minxiong/

例如：

station.c
market.c
temple.c

每個 Site：

set_site_id("minxiong_station");
set_settlement_id("minxiong");
Step 2

玩家進入：

FOOTPRINT_D->on_player_enter_site()

獲得：

geo:minxiong
Step 3

Event

FootprintGained

發布。

Step 4

Settlement 接收

memory +5
Step 5

look

顯示：

民雄

記憶度：
■■■■■■□□□□ 40%

文化度：
■■■□□□□□□□ 30%

完成後：

你就有真正能玩的東西。

Milestone 2
Site 系統正式化

目前文件大量提到：

World
Site
Settlement

但 Site 其實還沒有成為正式 Aggregate。

建議新增：

std/site.c

作為：

Site Aggregate Root

欄位：

site_id
settlement_id
era_id

memory_fragments
footprints

heritage_level

之後所有：

車站
廟宇
古道
學校
市場

都繼承它。

Milestone 3
Memory Fragment 系統

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

Milestone 4
Era Progression

目前：

timeline_d.c

已經存在。

但尚未由世界事件驅動。

建議：

全島記憶度
↓
40%
↓
解鎖下一 Era

例如：

v0_1 荒野福爾摩沙

↓ 40%

v0_2 海商時代

↓ 60%

v1_0 乙未戰爭
優先順序

我會按照下面順序做：

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

不要先做：

戰鬥
工會
技能樹
銀行
跨服
P2P

因為你的核心循環還沒成立。

目前最有價值的工作，是把 README 裡那條：

走進民雄老車站
↓
獲得踏印
↓
民雄記憶值 +5

真正跑起來。

只要這條鏈完成，整個《源流福爾摩沙》的設計理念就首次被驗證了。

問題一：不一致
問題現況應該tier 數值minxiong=4, lukang=6, tainan=9，三套不同邏輯統一定義name 欄位只有現代名，硬編碼改為 README-naming.md 的 names[] 結構Site yaml大多是空檔，只有 id + connections需要補齊欄位Era key 格式routes 用 v1.0，events 用 "v2.1"，eras 用 "v0_1"統一一種
問題二：路由重複
routes/settlements/ 和 routes/site/minxiong/ 是兩套系統，前者是聚落間，後者是聚落內 site 間，邏輯不同但格式相近，daemon 很難知道該讀哪個。
問題三：daemon 完全沒有讀這些 yaml 的邏輯
現有的 settlement_d.c 只讀 settlements/*.yaml，不知道 sites/、routes/、world/eras/ 的存在。

解法：先定標準，再改 daemon
第一步：統一 YAML Schema
我建議用一份文件定死格式，然後把現有的 yaml 對齊它。Schema 如下：
settlements yaml（加入 names[]，移除硬編碼 name）：
yamlid: minxiong
canonical_name: 民雄        # 永遠不變的內部識別名
tier: village               # village / town / city3 / city2 / city1
                            # 不再用數字，避免不同人用不同數字

names:
  - era: indigenous
    name: 打貓社
  - era: qing
    name: 打貓
  - era: japanese
    name: 民雄庄
  - era: modern
    name: 民雄鄉
sites yaml（補齊必要欄位）：
yamlid: minxiong_old_station
settlement: minxiong
canonical_name: 民雄車站
is_heritage: false

names:
  - era: japanese
    name: 民雄驛
  - era: modern
    name: 民雄火車站

connections:
  - minxiong_market
Era key 統一用 qing_early / qing_late / japanese / roc / modern（如 README-naming.md），不用 v1.0 這種版本號，因為版本號是遊戲概念，名稱是歷史概念，兩者不應混用。

第二步：daemon 的修改
需要改動三個 daemon，新增一個：
settlement_d.c 修改：

load_settlement() 讀到 names[] 後，快取成 era→name 的 mapping
新增 query_name_in_era(settlement_id, era_id) 方法
新增 load_sites_for_settlement(settlement_id) 方法（讀 sites/ 目錄）

site_d.c（新增）：

讀 data/yaml/sites/<settlement>/ 下所有 yaml
提供 get_connections(site_id)
提供 query_name_in_era(site_id, era_id)

route_d.c（新增）：

讀 routes/settlements/ → 聚落間移動（travel 指令用）
讀 routes/site/<settlement>/ → 聚落內移動（go 指令用）
提供 query_travel_time(from, to, transport_type)
提供 query_connections(site_id)

era_d.c（替代現有 timeline_d.c 的部分）：

讀 world/eras/
提供 query_current_era(player)
提供 resolve_name(entity_id, entity_type) → 這是核心，根據玩家當前 era 回傳正確名稱


resolve_name 是整個系統的核心
這個函式要放在哪裡值得想清楚。
因為「名稱隨 Era 變化」這件事，會被 site.c 的 do_look()、travel 指令、NPC 對話、地圖顯示全部用到，我建議把它放在 era_d.c：
c// era_d.c
string resolve_name(string entity_id, string entity_type, object player) {
    string current_era = query_player_era(player);
    
    // 從 yaml 快取的 names[] 找對應 era
    mapping names = _name_cache[entity_type + ":" + entity_id];
    if (!names) return _fallback_canonical(entity_id);
    
    // 找最接近的 era（不一定完全匹配，找最近的上溯 era）
    return _resolve_era_name(names, current_era);
}
「最近的上溯 era」的意思是：如果玩家在 qing_late，但 names[] 只有 qing 和 modern，就用 qing。不要報錯，要降級處理。

要我現在開始寫這三份文件嗎？

yaml_schema.md——所有 yaml 欄位的正式定義
site_d.c + route_d.c——兩個新 daemon
修改後的 settlement_d.c（加入 names[] 和 load_sites）
