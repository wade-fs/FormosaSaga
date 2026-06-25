# 《源流福爾摩沙》開發進度與 TODO

## 🎯 當前進展與 Milestone 狀態

| 里程碑階段 | 功能目標 | 狀態 | 備註 |
|:---|:---|:---:|:---|
| **P0** | 民雄垂直切片 (Minxiong Vertical Slice) | **✓ 已完成** | 成功實現踏印獲得、記憶度增長、地標探索 look 關聯 |
| **P1** | 地景與地標整合 (Site Aggregate) | **✓ 已完成** | 解放普通 LPC 實體，改由 YAML 驅動動態生成 12 個 Sites |
| **P2** | 歷史記憶碎片 (Memory Fragment) | **✓ 已完成** | 實作 `/data/yaml/memories/` YAML 載入，玩家抵達 Site 觸發共鳴並持久化存檔 |
| **P3** | 時代推展與主線機制 (Era Progression) | **進行中** | 設計 `timeline_d` 與全島記憶度 / 共鳴值的解鎖驅動 |
| **P4** | 職涯與勢力系統 (Profession / Faction) | **待執行** | 規劃 `career_d` 與 `faction_d` |
| **P5** | 失源者、危機與共鳴 (Specter / Oblivion / Resonance) | **待執行** | `oblivion_d`, `resonance_d` 設計 |

---

## 🛠️ 近期具體完成事項 (Milestone 1-3)
1. **動態 YAML 地標 (Site) 生成**：
   - 移除 redundant 的普通地標 LPC 檔案，全部轉移至 `/data/yaml/sites/minxiong/`。
   - 修改 site.c 與 settlement_d.c，當實體 `.c` 不存在時，動態複製通用地標並載入 YAML 內的 descriptions 與 reveal_layers。
2. **記憶碎片 (Memory Fragment) 機制實作**：
   - 建立 `/data/yaml/memories/`，放置歷史事件片段定義（如 `minxiong_station_001.yaml`）。
   - 在 user.c 新增 `unlocked_memories` 屬性與儲存機制，確保解鎖的記憶碎片持久化。
   - 擴充 memory_d.c，在玩家走入地標時自動判斷前置條件（例如：擁有某特定地理踏印），觸發記憶解鎖並發送 `MemoryCompleted` 事件，增加聚落的記憶值。
3. **VM 執行崩潰修復**：
   - 初始化 `footprint_atlas` 映射，完美解決了 Go MUD 伺服器啟動時的 SIGSEGV 指針崩潰。

---

## 📋 下一步規劃 (Milestone 4 - P3)
- **實作 Era 推進驅動**：
  - 完善 timeline_d.c 中的文明度計算與 Era 自動晉級。
  - 當玩家解鎖特定數量的記憶碎片或聚落平均記憶度達到一定百分比時，觸發時代跳轉（例如：解鎖民雄大正時期歷史層）。
