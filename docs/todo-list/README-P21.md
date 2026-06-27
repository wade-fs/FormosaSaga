  ## P21 — 歷史事件驅動的世界狀態 完成摘要                                       12:34:59 [14/735]
                                                                                                  
  ### 新增檔案                                                                                    
   檔案                                         | 說明                                            
  ----------------------------------------------|----------------------------------------------   
   world_state_d.c                               | 世界狀態守護進程（核心引擎）                   
   minxiong_sugar_chain.yaml                               | 民雄糖業演化線 YAML 定義             
   cmd_worldstate.c                               |  worldstate  查詢與管理指令                   
   test_world_state.c                               | P21 測試套件                                
                                                                                                  
  ### 修改檔案                                                                                    
   檔案                                         | 說明                                            
  ----------------------------------------------|----------------------------------------------   
   site.c                               |  do_look()  新增世界狀態描述注入                        
   formosa.h                               | 新增  WORLD_STATE_D  定義                            
  ──────
  ### 核心設計

  **世界狀態鏈（State Chain）**是一條由 Incident / Quest / Memory
  驅動的線性演化路徑。以民雄糖業為例：

    state_0 ──[minxiong_sugar_001 記憶解鎖]──▶ state_1
    state_1 ──[minxiong_sugar_incident 結案]──▶ state_2
    state_2 ──[sugar_railway_repair 任務完成]──▶ state_3
    state_3 ──[minxiong_heritage_documentation 完成]──▶ state_4

  每個狀態可執行的效果：

   效果類型                             | 說明
  --------------------------------------|------------------------------------------------------
    site_desc_inject                    | 在 look 時動態注入地點描述（取代硬切 Era）
    npc_spawn                           | 讓新 NPC 出現在指定地標
    npc_flag                            | 設定 NPC 旗標（供 schedule override 與對話條件使用）
    quest_unlock                        | 解鎖新任務（設定全域旗標）
    memory_unlock                       | 強制向在線玩家解鎖新記憶碎片
    site_unlock                         | 開放新地點（呼叫 route_d）
    settlement_boost                    | 提升聚落六維屬性值
    broadcast                           | 向全伺服器所有在線玩家廣播事件訊息

   worldstate  指令介面：

  •  worldstate  — 以進度條顯示所有狀態鏈的目前位置
  •  worldstate minxiong_sugar_chain  — 顯示完整的五段演化狀態與描述
  •  worldstate advance <chain> <state>  /  worldstate reset <chain> — 管理員工具
