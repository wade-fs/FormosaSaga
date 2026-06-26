# 《源流福爾摩沙》開發進度與 TODO

## 🎯 當前進展與 Milestone 狀態

| 里程碑階段 | 功能目標 | 狀態 | 備註 |
|:---|:---|:---:|:---|
| **P0** | 民雄垂直切片 (Minxiong Vertical Slice) | **✓ 已完成** | 踏印獲得、記憶度增長、地標探索 look 關聯 |
| **P1** | YAML 驅動動態地標 (Site Aggregate) | **✓ 已完成** | 普通 LPC 地標解放為 YAML，`settlement_d` 動態複製生成 12 個 Sites |
| **P2** | 歷史記憶碎片系統 (Memory Fragment) | **✓ 已完成** | `memory_d` + `/data/yaml/memories/` YAML，玩家觸發共鳴並持久化存檔 |
| **P3** | 時代推展機制 (Era Progression) | **✓ 已完成** | `MemoryCompleted` 事件驅動 `world_progress`，達門檻自動觸發 `next_era()` |
| **P4** | 職涯與勢力系統 (Profession / Faction) | **✓ 已完成** | `career_d` + YAML 四職涯（農商匠文），`faction_d` + 三勢力（劉家/糖業/廟委），事件驅動自動累積修練點 |
| **P5** | 失源者、危機與共鳴 (Specter / Oblivion / Resonance) | **✓ 已完成** | `oblivion_d`（週期衰減+危機廣播）、`resonance_d`（多人共鳴）、`/std/specter.c`（可互動物件）、`cmd_commune` |
| **P7** | 新手任務與引導流程 (Tutorial Quest) | **✓ 已完成** | 以民雄「老站長」實作探索地標 -> 獲得踏印 -> 任務回報循環 |

---

## 🛠️ 已完成事項摘要

### P0 — 民雄垂直切片
- 實作踏印 (`footprint_d`) 與踏印圖譜 (`footprint_atlas`) 持久化。
- 修復啟動時 `footprint_atlas` nil 指針崩潰 (SIGSEGV)。

### P1 — YAML 驅動地標
- 移除所有普通 LPC 地標檔案，改由 `/data/yaml/sites/minxiong/` 驅動（12 個 YAML 地標）。
- `settlement_d.c:get_site_object` 作工廠：優先找 `.c` 實體，其次動態 `clone_object("/std/site.c")` + `setup_from_yaml()`。

### P2 — 歷史記憶碎片
- 建立 `/data/yaml/memories/`，放置記憶片段定義（含觸發地標、前置條件、進度權重）。
- `user.c` 新增 `unlocked_memories` 屬性，確保跨登入持久化。
- `memory_d.c` 在玩家進入地標時自動比對 `trigger_site`、前置條件並觸發解鎖。

### P3 — 時代推展
- **事件鏈完整打通**：
  - `memory_d.c` 解鎖後呼叫 `EVENT_D->publish("MemoryCompleted", {..., "progress": N})`。
  - `timeline_d.c` 訂閱 `MemoryCompleted`，在 `on_memory_completed()` 裡累加 `world_progress`。
  - 達到 YAML `min_progress` 門檻後自動呼交 `next_era()`，廣播並發送 `EraShifted` 事件。
- **資料驅動門檻**：`min_progress` 由各時代 YAML 設定，非硬編碼。
- **民雄記憶地圖**：新增 6 則記憶片段覆蓋 `ghost_house`、`sugar_factory_ruins`、`dashiye_temple`，構成完整解鎖路徑。
- **`memory` 玩家指令**：新增 `cmd_memory.c`，可列出記憶清單、查看時代進度、閱讀片段全文。

### P6 — 跨區域地圖與地理網絡擴展
- 修正 `route_minxiong_chiayi.yaml` 中屬性名稱 `notes` 改為 `nodes` 錯誤。
- 實作嘉義市主聚落地標 (`chiayi_city.yaml`) 與附屬 Sites（`chiayi_city_temple.yaml`、`chiayi_train_station.yaml`），補全與美化設定與描述。
- 實作新港鄉主聚落地標 (`singang.yaml`) 與其附屬 Site `singang_market.yaml`（替代舊 `singang_site.yaml`），修正新港聚落 `singang.yaml` 的 sites 清單。
- 完善 `std/site.c` 處理無 `entity_id` 玩家造成的 nil map indexing 執行期異常。
- 調整 `testlib` 測試環境，補全必要的 `std` 繼承檔案與 `daemon/yaml` 軟連結，確保核心測試（276/276）在 MudScript 模式下完全通過。

### P7 — 新手任務與引導流程
- 以民雄的「老站長」為核心，實作新手引導任務「老站長的心願」。
- 修復 `footprint_atlas` 存檔問題，移除 `std/user.c` 內多餘宣告以避開序列化引擎死角。
- 更新了 `testlib/std/user.c` 軟連結，確保自動測試環境吃到所有最新修改。
- `minxiong_old_station.yaml` 中移除自動賦予糖鐵踏印的邏輯，移至 `minxiong_market.yaml`，確保「探索市集獲取踏印 -> 回報車站」的邏輯順暢。
- 補全 `test_quest_loop.c` 整合測試並確認全部通過。

---

## 📋 下一步規劃

### P8 — 職涯動作與勢力事件玩法深化
- [x] 實作不同職涯（農商匠文）的專屬動作或命令（已完成 `cmd_farm.c`, `cmd_trade.c`, `cmd_craft.c`, `cmd_record.c`，並緊密結合歷代台灣產業脈絡）。
- [x] 設計與實作「廟委鎮煞委託」任務（含前置任務鎖定、組隊秘境線索、收集鎮符石回報、聲望與護符獎勵）與完整流程整合測試。
- [x] 設計與實作「糖鐵搶修委託」任務與整合測試（已完成，詳見 [sugar_railway_repair.md](quests/sugar_railway_repair.md)）。
- [x] 設計各大勢力（劉家、糖業、廟委）的聲望影響與專屬派系任務。（劉家地契委託、糖鐵搶修委託、廟委鎮煞委託均已實作並通過整合測試）
- [x] 設計週期性的「遺忘浪潮」危機事件與失源者（Specter）互動/共鳴儀式（已完成設計規劃，詳見 [oblivion_and_resonance.md](quests/oblivion_and_resonance.md)）。
- [ ] 依設計實作週期性的「遺忘浪潮」危機事件與失源者共鳴儀式整合測試與功能。

