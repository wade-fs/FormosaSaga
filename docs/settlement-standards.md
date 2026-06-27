# 聚落驗收分級標準 (Settlement Definition of Done)

> 追蹤工具：`python3 check_settlement.py <id>` 或 `make audit-settlement SETTLEMENT=<id>`

---

## 一、為什麼需要分級？

民雄（村落）與台南（直轄市）不應套同一標準。
分級的依據有二：

- **行政層級**：直轄市 > 縣轄市 > 重要城鎮 > 特色鄉村 > 路過據點
- **故事地位**：某些小地方因為歷史事件而超越行政層級（如霧社、玉井）

---

## 二、分級門檻表

> 單位：最低數量。`-` 代表無強制要求，有亦加分。

| 指標 | S 直轄大城 | A 重要市鎮 | B 特色鄉村 | C 路過據點 |
|---|:---:|:---:|:---:|:---:|
| **tier 數值** | 1 | 2–3 | 4 / town | village / C |
| **Sites（地標）** | 50 | 25 | 12 | 5 |
| **NPCs（登場人物）** | 60 | 25 | 12 | 4 |
| **Incidents（歷史事件）** | 12 | 6 | 3 | 1 |
| **Memories（記憶碎片）** | 40 | 20 | 8 | 3 |
| **Quests（任務故事）** | 30 | 12 | 5 | 1 |
| **Rumors（傳言）** | 20 | 10 | 4 | - |
| **Dynamic Events（動態事件）** | 8 | 4 | 2 | - |
| **Hidden Areas（隱藏地區）** | 6 | 3 | 1 | - |
| **Era ≥3 層 / Site 達標率** | 60% | 40% | 20% | - |

> **長遠願景**（全成熟態）：上表乘以 1.5～2 倍，不作為開放條件。

---

## 三、Tier 對照（全島 34 個聚落）

### Tier S — 直轄大城（6 個）
> 門檻最高，卷三以後才需全力填充

| ID | 名稱 | 主要登場卷次 | 開發優先 |
|---|---|---|---|
| `taipei` | 台北 | 卷三、卷六 | ⬜ 低 |
| `tainan` | 台南 | 卷一、卷三 | 🟠 中 |
| `kaohsiung` | 高雄 | 卷二、卷六 | ⬜ 低 |
| `taichung` | 台中 | 卷二、卷六 | ⬜ 低 |
| `new_taipei` | 新北 | 卷六 | ⬜ 低 |
| `taoyuan` | 桃園 | 卷六 | ⬜ 低 |

### Tier A — 重要市鎮（13 個）
> 各卷的地區樞紐

| ID | 名稱 | 主要登場卷次 | 開發優先 |
|---|---|---|---|
| `chiayi_city` | 嘉義市 | 卷一（卷一核心） | 🔴 高 |
| `changhua` | 彰化縣 | 卷一、卷二 | 🟠 中 |
| `yunlin` | 雲林縣 | 卷二 | 🟡 次 |
| `miaoli` | 苗栗縣 | 卷二 | 🟡 次 |
| `pingtung` | 屏東縣 | 卷二 | 🟡 次 |
| `hsinchu_city` | 新竹市 | 卷三 | ⬜ 低 |
| `keelung` | 基隆市 | 卷三 | ⬜ 低 |
| `hualien` | 花蓮縣 | 卷四 | ⬜ 低 |
| `taitung` | 台東縣 | 卷四 | ⬜ 低 |
| `yilan` | 宜蘭縣 | 卷三 | ⬜ 低 |
| `penghu` | 澎湖縣 | 卷五 | ⬜ 低 |
| `kinmen` | 金門縣 | 卷五 | ⬜ 低 |
| `lianjiang` | 連江縣 | 卷五 | ⬜ 低 |

### Tier B — 特色鄉村（13 個）
> 具獨特歷史事件，故事地位超越行政層級

| ID | 名稱 | 主要登場卷次 | 開發優先 | 特色事件 |
|---|---|---|---|---|
| `minxiong` | 民雄鄉 | 卷一（新手村） | 🔴 最高 | 糖業興衰、劉家鬼屋 |
| `singang` | 新港鄉 | 卷一 | 🔴 高 | 西拉雅族記憶 |
| `lukang` | 鹿港鎮 | 卷一 | 🟠 中 | 工匠職涯、乙未前夕 |
| `changhua_city` | 彰化市 | 卷一、卷二 | 🟠 中 | 八卦山戰役 |
| `nantou_wushe` | 霧社 | 卷四 | 🟡 次 | 霧社事件 |
| `tainan_yujing` | 玉井（噍吧哖） | 卷四 | 🟡 次 | 西來庵事件 |
| `ludao` | 綠島 | 卷五 | 🟡 次 | 白色恐怖 |
| `xinshi` | 台南新市 | 卷一 | 🟡 次 | 西拉雅新港社 |
| `shanhua` | 台南善化 | 卷一 | ⬜ 低 | — |
| `jiali` | 台南佳里 | 卷一 | ⬜ 低 | — |
| `alishan` | 阿里山 | 卷三 | ⬜ 低 | — |
| `meishan` | 梅山 | 卷三 | ⬜ 低 | — |
| `dongshi` | 東石 | 卷三 | ⬜ 低 | — |

### Tier C — 路過據點（2 個）
> 故事中短暫出現，最低門檻

| ID | 名稱 | 登場卷次 | 備註 |
|---|---|---|---|
| `lanyu` | 蘭嶼 | 卷五 | 原住民生態保護區 |
| `lianjiang` | 連江（馬祖） | 卷五 | 特殊軍事背景 |

---

## 四、卷一完成條件（開放卷二前的底線）

```
卷一完成 = 下列所有聚落達到各自 Tier 的 80% 以上

  🔴 minxiong        → Tier B 80%
  🔴 chiayi_city     → Tier A 80%（需建立）
  🟠 singang         → Tier B 80%
  🟠 tainan（安平）  → Tier S 50%（主線骨幹即可）
  🟠 lukang          → Tier B 80%
  🟠 changhua_city   → Tier B 80%（八卦山）
```

驗收指令：
```bash
make audit-settlement SETTLEMENT=minxiong
make audit-settlement SETTLEMENT=chiayi_city
make audit-settlement SETTLEMENT=singang
make audit-settlement SETTLEMENT=tainan
make audit-settlement SETTLEMENT=lukang
make audit-settlement SETTLEMENT=changhua_city
```

---

## 五、開發優先順序建議

```
階段 1（現在）：把民雄填充到 Tier B 80%
  → 目前：1/9 通過（僅 Sites 達標）
  → 需要：NPCs×12、Memories×8、Quests×5、Incidents×3

階段 2：嘉義市 Tier A 基本盤
  → 城隍廟、火車站、中央噴水池、北門圓環一帶地標

階段 3：新港＋安平骨架填充
  → 新港西拉雅線、安平荷蘭時代層

階段 4：鹿港＋彰化市主線
  → 乙未戰爭場景、工匠職涯觸發點

階段 5：開放卷二開發（TODO-vol2.md）
```

---

*最後更新：2026-06-27*
*對應腳本：`check_settlement.py`（支援 `--tier` 參數自動套用分級門檻）*
