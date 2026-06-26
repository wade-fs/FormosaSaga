# 源流福爾摩沙 (Formosa Saga) 🇹🇼

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![LPC Driver](https://img.shields.io/badge/Driver-Golang_MudOS_v22-00ADD8.svg?logo=go)]()
[![Status: Active](https://img.shields.io/badge/Status-Active_Development-orange.svg)]()

> **「尋回失落的記憶，重塑歷史的輪廓。」**

**源流福爾摩沙 (Formosa Saga)** 是一款基於 **Golang 自行實作的 MudOS v22 模擬引擎** 所開發的現代化文字化身角色扮演遊戲 (MUD)。本作打破傳統 MUD 的硬編碼泥淖，導入了高度靈活的 **YAML 驅動架構**，並結合了台灣豐富的歷史文化背景。玩家將化身為「尋源者」，穿梭於清領、日治與現代的不同時空，收集歷史記憶的碎片，抵禦試圖抹消歷史的「遺忘浪潮」。

---

## ✨ 核心特色 (Features)

### 📜 **資料與邏輯分離的現代化架構 (YAML-Driven)**
揮別過去一個房間一個 `.c` 檔案的時代。Formosa Saga 實作了強大的 `settlement_d` 與 `site_d` 系統，所有的地標、NPC、甚至是記憶片段，皆可透過簡潔的 YAML 檔案進行配置。讓企劃與腳本作者不需懂 LPC 也能輕鬆創造世界。

### 🕰️ **動態時代推演 (Dynamic Era Progression)**
隨著玩家社群共同解鎖「歷史記憶碎片」，伺服器的「時代進度」將不斷推進。從清領時期的「打貓街市」到日治時期的「民雄驛」，整個世界會根據當前時代動態切換場景描述、NPC 與可探索的區域。

### 🧩 **踏印與記憶系統 (Footprints & Memories)**
- **踏印 (Footprints)**：透過實地「探索」(Travel & Look) 台灣各地的名勝古蹟（如民雄鬼屋、大士爺廟），獲取專屬踏印。
- **記憶 (Memories)**：集齊特定踏印後，觸發歷史的「共鳴」，解鎖不為人知的歷史記憶，推動世界的進程。

### ⚔️ **陣營與職涯 (Factions & Careers)**
- **四大職涯**：農、商、匠、文。累積修練點數，解鎖專屬的職涯技能與互動指令。
- **三大勢力**：加入在地仕紳的「劉家」、掌握經濟命脈的「糖業」、或是維繫信仰的「廟委」，爭奪區域的影響力。

### 👻 **失源者與遺忘浪潮 (Specters & Oblivion)**
歷史的缺口會產生「失源者」。伺服器會定期爆發「遺忘浪潮」危機，玩家必須齊心協力發起「共鳴儀式」，阻止歷史被徹底抹消。

### ⚔️ **任務與引導系統 (Quests & Tutorials)**
- **老站長的心願（新手引導）**：帶領玩家探索民雄老街，獲得糖鐵遺址踏印並向老站長回報完成任務，藉此熟悉探索與時代推進的基本循環。詳見 [tutorial_quest.md](docs/quests/tutorial_quest.md)。
- **廟委鎮煞委託（勢力任務模板）**：要求等級 5 且完成前置引導任務。需與同伴組隊才能在大士爺廟察覺地下陣法線索，進入秘境收集「鎮符石」，回報完成後可獲得大士爺護符與廟委聲望。詳見 [temple_exorcism.md](docs/quests/temple_exorcism.md)。
- **糖鐵搶修委託（已完成）**：要求等級 6 且完成前置任務。玩家需與同伴在甘蔗林尋找脫軌的五分車火車頭並收集零件完成搶修，完成後可獲得紀念徽章與糖業組合聲望。詳見 [sugar_railway_repair.md](docs/quests/sugar_railway_repair.md)。
- **劉家地契委託（已完成）**：要求等級 7 且完成前置任務。玩家需與同伴前往民雄鬼屋尋找隱藏的隔間，收集劉家遺失的地契，完成後可獲得劉家家徽戒指與劉家聲望。詳見 [liu_deed_recovery.md](docs/quests/liu_deed_recovery.md)。

---

## 🚀 快速開始 (Getting Started)

想親自體驗或參與開發這款充滿台灣歷史韻味的現代 MUD 嗎？

### 1. 系統需求
- **Golang 1.22+** (由於底層為 Golang 實作的 MudOS v22 模擬器，需安裝 Go 環境)
- **Make** 工具

### 2. 下載與啟動
將專案 Clone 到本地：
```bash
git clone https://github.com/YourUsername/FormosaSaga.git
cd FormosaSaga
```

啟動伺服器：
```bash
# 啟動 MUD 伺服器
make run
```
預設會監聽 `8080` 埠，本作純粹使用瀏覽器連線遊玩，請打開瀏覽器前往 `http://127.0.0.1:8080`，無須使用 telnet 或傳統 MUD 客戶端。

### 3. 自動化測試
我們極度重視程式碼品質與架構穩定性。專案內建完整的單元測試與整合測試框架：
```bash
# 執行 LPC 核心驅動測試
make test-driver

# 執行自動化整合場景測試
make test-fsmud
```

---

## 📂 專案結構 (Project Structure)

```text
FormosaSaga/
├── mudlib/                  # MUD 核心程式碼
│   ├── master.c             # LPC 核心控制與權限管理入口
│   ├── include/
│   │   ├── config.h         # 系統全域參數設定
│   │   └── formosa.h        # 源流福爾摩沙專屬巨集與常數定義
│   ├── daemon/              # 核心守護進程 (Daemon)
│   ├── std/                 # 基礎繼承物件 (User, Site, NPC...)
│   └── data/yaml/           # YAML 設定檔 (Sites, Memories, Factions)
├── testlib/                 # 自動化測試專用環境與腳本
├── docs/                    # 開發文件與 TODO
├── chapters/                # 小說
├── Makefile                 # 自動化建置與測試腳本
└── README.md                # 專案說明
```

---

## 🤝 參與貢獻 (Contributing)

我們非常歡迎任何形式的貢獻！無論是：
- ✍️ **編寫腳本**：透過 YAML 新增台灣各地的歷史地標或記憶碎片。
- 💻 **程式開發**：優化 LPC 核心系統，實作新的 Efuns 或系統模組。
- 🐛 **回報問題**：提交 Issue 告訴我們哪裡可以做得更好。

詳情請參考 `docs/TODO.md` 中尚未完成的 Milestone 規劃，並隨時發起 Pull Request！

---

## 📜 授權條款 (License)

本專案採用 [MIT License](LICENSE) 授權。
