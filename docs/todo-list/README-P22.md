# P22 — 內容可視化配置工具 (Content Authoring Tools)

## 🎯 目標與概述
本階段的目標是開發一個專屬的「內容可視化配置工具」，協助企劃與開發人員更直觀地編輯、管理與概覽世界內容（YAML 檔案），而不需要直接面對原始碼。

## ✨ 核心功能
1. **互動式地圖網絡 (Visual Graph)**: 透過 Force-directed Graph 等視覺化方式，展示聚落 (Settlement) 下各地標 (Site) 的連接關係與路線。
2. **YAML 內容編輯器 (Content Editor)**: 提供專屬的介面來瀏覽、修改 Sites、NPCs、Memories、Incidents 等 YAML 內容。
3. **全域內容概覽 (Dashboard)**: 以視覺化的方式呈現各聚落的完成度、地標數量、記憶碎片進度等指標。
4. **快速建立模板 (Scaffolding UI)**: 透過表單式介面，一鍵生成新的地標、任務、NPC 等 YAML 檔案模板。

## 🛠️ 實作細節
- **檔案位置**: `/mudlib/web/static/author.html`
- **架構設計**: 
  - 延續專案的 WebSocket 通訊架構 (`/ws`)，與 MUD 伺服器進行溝通。
  - 採用純 HTML/CSS/JS 開發，不依賴龐大的前端框架，維持輕量與高效。
  - 使用 D3.js 或 Cytoscape.js 等輕量級視覺化庫來渲染關係圖（如果透過 CDN），或使用原生的 Canvas/SVG 實作。
  - 整合現有的 Monaco Editor 提供進階的 YAML 語法高亮與編輯功能。

## 📝 驗收標準
- [x] 提供獨立的 `author.html` 頁面供開發者使用。
- [x] 頁面具備現代感（深色主題、Glassmorphism 等）且支援繁體中文。
- [x] 能透過 WebSocket 與伺服器連線，並取得必要的檔案列表。
- [x] 具備內容預覽與編輯的基本框架。
