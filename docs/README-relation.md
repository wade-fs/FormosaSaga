```
Settlement（聚落）
  有六維數值
  有人口
  有失源者
  玩家可以定居
  對應行政區（鄉/鎮/市/區）
  
  └── Site（地點）
        沒有六維（繼承所屬 settlement 的脈絡）
        有歷史層
        有記憶碎片
        有 NPC
        玩家進入探索，不定居
        
        └── HistoryLayer（歷史層）
              同一個 site 在不同 era 的樣貌
              由 era + site_id 組合定位
              玩家需要條件才能進入
```

按照這個原則，補幾個邊界案例的判斷：
```
大稻埕    → Site（屬於 settlement: taipei_datong）
            大稻埕是台北大同區的一個街區，不是獨立行政區

艋舺      → Site（屬於 settlement: taipei_wanhua）

鹿耳門    → Site（屬於 settlement: tainan_anan）
            安南區的一個歷史地點

馬赫坡社  → Site（屬於 settlement: nantou_renai）
            仁愛鄉內的賽德克部落遺址

八卦山    → Site（屬於 settlement: changhua）

綠島監獄  → Site（屬於 settlement: ludao）
            綠島本身是 settlement，監獄是其中的 site

霧社      → 這裡比較複雜：
            霧社（仁愛鄉霧社村）→ Settlement
            霧社公學校運動場   → Site（屬於 settlement: wushe）
            馬赫坡社          → Site（屬於 settlement: wushe）
```
