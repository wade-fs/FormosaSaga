# 世界演化與內容驅動引擎：MUD 架構設計思考

這是一份針對 Mudlib 定位與架構設計的思考整理。核心觀點在於：本專案的 Mudlib 並非單純的「適合歷史題材」，其本質是一個 **以世界狀態（World State）為核心的內容驅動引擎（Content-driven World Engine）**。

---

## 1. 傳統 MUD vs. 本專案 Mudlib

### 傳統 MUD 的核心 (靜態世界)
傳統 MUD 的架構與玩法通常是圍繞著以下結構：
```
Room ➔ NPC ➔ Monster ➔ Item
```
玩家的遊戲循環為：
```
走路 ➔ 打怪 ➔ 掉寶 ➔ 升級
```
在這種模式下，世界本身是**靜態不變**的。

### 本專案 Mudlib 的核心 (世界演化)
本專案的架構重點在於：
```
Settlement ➔ Site ➔ Memory ➔ Era ➔ Event
```
NPC 與 Quest 反而是附屬。這代表了**世界是會演化（World Evolution）的**。

---

## 2. 適用題材分類與相容性分析

基於「世界演化」的核心特徵，不同題材的適合度如下：

### 第一類：歷史演化 (★★★★★)
- **代表題材**：台灣史（目前專案）、三國、戰國、日本幕末、羅馬帝國、歐洲中世紀。
- **適用原因**：這類題材皆具備「年代 ➔ 事件 ➔ 勢力 ➔ 人物 ➔ 地圖」的演進結構，可以直接套用此架構。
  - *以三國為例*：`洛陽 ➔ 董卓 ➔ 火燒洛陽 ➔ 曹操入許昌 ➔ 赤壁 ➔ 三國鼎立`，這本質上就是 `Incident ➔ Era` 的演進。

### 第二類：城市經營 (★★★★☆)
- **代表題材**：模擬城市類型的聚落與居民模擬。
- **適用原因**：`Settlement` 直接對應聚落，而 `Site` 可以靈活對應如 `Market`（市場）、`School`（學校）、`Temple`（寺廟）、`Dock`（碼頭）等，配合事件與居民系統即可運作。

### 第三類：開放世界 RPG (★★★★☆)
- **代表題材**：*Skyrim*、*Gothic*、*Kingdom Come*。
- **適用原因**：這些遊戲高度依賴 `Site`（地點/遺跡/據點）作為內容載體與探索核心。

---

## 3. 與「蜀山/修仙/武俠」題材的相容性與擴充方案

### 為什麼「蜀山/修仙」只有 60% ~ 70% 的相容性？
其原因並非題材本身（修仙），而是**空間與實體模型不同**：
- **蜀山/修仙世界模型**：`宗門 ➔ 洞府 ➔ 秘境 ➔ 法寶 ➔ 功法 ➔ 境界`。
- **核心實體（Entity）的差異**：
  - 本系統目前最大的 Entity 是 **`Site`** 或 **`World`**。
  - 修仙類遊戲最大的 Entity 是 **`Character`**（角色）。所有要素（境界、靈根、悟性、飛劍、法寶、丹藥、神識、壽元、天劫）都圍繞著角色轉，而非世界。
  - 玩家的遊戲循環通常是：`閉關 ➔ 煉丹 ➔ 煉器 ➔ 悟道 ➔ 渡劫`，而不是以探索 `Site` 與 `Memory` 為主。

### 擴充方案：新增玩法層
不需要重構現有架構，而是**新增一層角色修煉系統（Cultivation System）**，使其與現有的世界系統並存：

```
世界層 (保持不變)：
World ➔ Settlement ➔ Site

角色/修煉層 (新增)：
Character ➔ Root ➔ Cultivation ➔ Technique ➔ Artifact ➔ Tribulation
```

---

## 4. 走向類 ECS (Entity Component System) 架構

本 Mudlib 的 Engine 設計已經開始展現 ECS 的特質（以組裝代替繼承）：

- **Entity & Component 組裝範例**：
  - **`Settlement / Site`** 可以附帶：`Location`、`Memory`、`Quest`、`NPC`、`Era` 等 Component。
  - **`NPC`** 可以附帶：`Profession`、`Faction`、`Rumor`、`Schedule`、`Relationship` 等 Component。

這讓世界元件可以自由組合，而非依賴硬編碼的類別繼承。

---

## 5. 三層架構設計與定位

本架構在實作上可被清晰拆分為三層：

```
┌────────────────────────────────────────────────────────┐
│ 第一層：Engine (底層)                                   │
│ (Event Bus, Daemon, Scheduler, Persistence, World, User)│
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│ 第二層：Data-driven Layer (資料驅動層，核心價值所在)    │
│ (Settlement, Site, NPC, Quest, Memory, Era, Faction)   │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│ 第三層：Gameplay Module (玩法模組層)                    │
│ ├─ 歷史模組 (Memory, Era, Incident)                     │
│ ├─ 修仙模組 (Cultivation, Realm, Technique)             │
│ ├─ 武俠模組 (Sect, Meridian, Internal Skill)            │
│ └─ 科幻模組 (Planet, Technology, Research)              │
└────────────────────────────────────────────────────────┘
```

### 核心價值：Everything is Content (資料定義世界)
- **傳統 MUD**：在程式碼中撰寫 `object room = create_room(...)` 或 `inherit NPC;`。
- **本系統**：使用 `site`、`quest`、`npc`、`era`、`memory` 等 YAML 設定檔來宣告。
- **資料與引擎分離**：YAML 僅是其中一種實作（第一個 Backend）。未來若改用 `JSON`、`TOML`、`SQLite`、`PostgreSQL`，甚至是 `Google Sheet` 匯出，底層 `Runtime` 與 `Loader` 也幾乎不需要修改。企劃人員完全不需要觸碰 LPC 程式碼。

因此，本專案更適合命名為 **World Content Engine (WCE)** 或 **Content-driven MUD Engine**。

---

## 6. 未來開發的指導原則

> **「世界是由資料定義，而不是由程式定義。」**

在未來新增任何系統或功能時，應優先問自己一個問題：
> **「這是一個新的 Engine 能力，還是一種新的 Content？」**

如果答案是**後者（Content）**，請務必將其優先設計為**資料格式（如 YAML/JSON）**，而非新增硬編碼程式碼。如此一來，Mudlib 才能真正成為一個可重用、可換題材的內容引擎，而不僅僅是適用於單一遊戲專案的程式庫。
