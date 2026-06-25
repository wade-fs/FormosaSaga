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
  - 達到 YAML `min_progress` 門檻後自動呼叫 `next_era()`，廣播並發送 `EraShifted` 事件。
- **資料驅動門檻**：`min_progress` 由各時代 YAML 設定，非硬編碼。
- **民雄記憶地圖**：新增 6 則記憶片段覆蓋 `ghost_house`、`sugar_factory_ruins`、`dashiye_temple`，構成完整解鎖路徑。
- **`memory` 玩家指令**：新增 `cmd_memory.c`，可列出記憶清單、查看時代進度、閱讀片段全文。

---

## 📋 下一步規劃

### P4 — 職涯與勢力系統
- 規劃 `career_d`（農、商、匠、武）與 `faction_d`（家族、聚落、幫派）。
- 職涯影響記憶解鎖條件（例如：「匠」職能解鎖更深層的工藝記憶）。
- 勢力關係影響聚落的記憶復原速度與遺忘危機速率。

### P5 — 失源者、危機與共鳴
- `oblivion_d`：當聚落記憶度低於 `OBLIVION_SPECTER` 閾值時，生成失源者 (Specter)。
- `resonance_d`：玩家之間可互相傳遞記憶，觸發共鳴加速效果。
- 危機事件系統：設計週期性觸發的全島遺忘危機，需玩家協力解除。
