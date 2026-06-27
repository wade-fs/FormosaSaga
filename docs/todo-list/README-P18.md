P18 — 地點與聚落探索度 (Site & Settlement Completion) 的開發！                 
具體完成的項目與系統變更如下：                                                                    

  1. 新增探索度計算核心守護進程 ( COMPLETION_D )
      • 建立  /daemon/completion_d.c ，專門負責將玩家的「地理足跡」與「已解鎖記憶
      (Evidence)」進行動態換算，回傳精確的百分比。
      • 單一地標的進度包含：「是否有親身造訪該地點
      (基礎探索)」與「該地點所有埋藏的記憶是否都已尋獲」。
      • 宏觀聚落的進度則是將該聚落下所有地標的進度彙整，算出一個總體的  Settlement Completion
      。                                          
  2. 追蹤玩家造訪紀錄
      • 擴充了  /std/site.c  核心場景檔：現在玩家只要執行  travel  或  enter 
      進入某個地點時，系統便會自動呼叫  record_exploration()  記錄下這個精確的地標
      ID，為探索度提供判斷依據。                  
      • 擴充  /daemon/site_d.c  與  /daemon/memory_d.c ，開放了  query_all_sites()  等 API
      讓進程能夠讀取所有 YAML 設定來計算「分母」（也就是世界總共有多少地標跟記憶可以收集）。
  3. 新增  explore  探索介面指令                  
      • 建立  /cmds/player/cmd_explore.c ，提供玩家查詢長期探索目標的介面：
          •  explore : 顯示當前所在的單一地標進度（例如： 目前地標：民雄鬼屋  進度：63%
          ），以及當前聚落的總體進度（例如： 所屬聚落：民雄  總進度：83% ）。
          •  explore list :                       
          會列出目前聚落（例如民雄）內所有的地點，並以列表呈現各個地點各自的完成度，若達 100%
          則會以亮綠色特別標記，方便玩家針對還未探索完畢的死角進行攻略。
