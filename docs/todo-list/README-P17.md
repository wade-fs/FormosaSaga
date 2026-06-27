P17 — 記憶碎片實體化與證據鏈 (Memory to Evidence) 的開發！                     
                                                                                                  
  具體完成的項目與變更如下：

  1. 記憶實體化為證據 (Evidence)
      • 擴充了  mudlib/data/yaml/memories/*.yaml  的結構，為記憶碎片新增了  evidence_type 
      屬性。
      • 例如  minxiong_ghost_001  (劉家的繁盛) 成為了  【老照片】 ， minxiong_ghost_002 
      (劉家的衰落) 成為了  【鄉野傳言】 ，而  minxiong_sugar_001  (打貓製糖所的煙囪) 則被定為
      【舊藍圖】 。
  2. 玩家取得提示與指令介面升級
      • 修改了  memory_d.c 
      守護進程，現在當玩家在場景中觸發記憶時，不再只顯示為無形的「記憶片段」，而是會明確提示：
      【證據尋獲】歷史的殘留化為實體，你獲得了一份關鍵證據 [老照片] 。
      • 升級了  memory  玩家指令 ( cmd_memory.c )，將原本的記憶選單標題改為
      「歷史記憶與證據卷宗」，並在列表與詳細資訊中清楚標示每份證據的形式（如  [老照片] 、
      [舊藍圖]  等）。
  3. 實作證據收集鏈以解鎖歷史真相 (Historical Truth)
      • 為了完美串連 P16 開發的事件系統與本次的 P17 證據化記憶，我全新設計了 「民雄鬼屋傳說
      (minxiong_ghost_incident)」 這個事件 ( minxiong_ghost_incident.yaml )。
      • 該事件完全依賴玩家在鬼屋收集到的多個記憶證據（即  ghost_diary_1  與  ghost_rumor_1
      ，對應上述的兩份記憶）作為串連。
      • 當玩家收集齊這些「證據」後，即可透過「歷史推理」( incident resolve ) 推進 100%
      的進度，解鎖關於劉家古厝並非厲鬼作祟，而是因為二戰轟炸與戰後蕭條而沒落的真正 Historical
      Truth。
      • 同時也順便修正了  minxiong_sugar_incident  之前遺留下來對記憶 ID 參照錯誤的問題。
