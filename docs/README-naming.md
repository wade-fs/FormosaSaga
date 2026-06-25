
id 與名稱分開，而且把名稱放進歷史資料：

# 聚點 - 嘉義
id: chiayi
canonical_name: 嘉義
type: settlement
names:

  - era: qing_early
    name: 諸羅

  - era: qing_late
    name: 諸羅城

  - era: late_qing
    name: 嘉義

  - era: japanese
    name: 嘉義街

  - era: modern

# 聚點 - 民雄
id: minxiong
canonical_name: 民雄
type: settlement
names:

  - era: indigenous
    name: 打貓社

  - era: qing
    name: 打貓

  - era: japanese
    name: 民雄庄

  - era: modern
    name: 民雄鄉
    name: 嘉義市

# Site 聚點內的地點-車站
id: minxiong_station
canonical_name: 民雄車站
type: site
settlement: minxiong
names:

  - era: japanese
    name: 民雄驛

  - era: roc
    name: 民雄車站

  - era: modern
    name: 民雄火車站

# 聚點到聚點間的交通 - 公路
id: route_settlement_minxiong_chiayi
names:

  - era: qing
    name: 打貓往諸羅官道

  - era: japanese
    name: 嘉義街道

  - era: modern
    name: 嘉民公路

# 聚點到聚點間的交通 - 鐵路
id: route_minxiong_chiayi_rail

type: route

network: west_line

nodes:
  - minxiong_station
  - chiayi_station

names:

  - era: japanese
    name: 縱貫線嘉義打貓段

  - era: modern
    name: 縱貫線民雄嘉義段

# 名稱永遠從 Era Overlay 查詢。

這樣玩家在 1700 年看到的是：

打貓

1905 年看到的是：

民雄庄

2026 年看到的是：

民雄鄉

但底層永遠都是同一個 Settlement：

id: minxiong

這樣你的世界資料庫才能支撐真正的歷史演進，而不會被現代地名綁死。
