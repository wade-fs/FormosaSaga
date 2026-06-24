// cmd/test-fsmud/main.go
package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"log"
	"net/url"
	"os"
	"os/exec"
	"strings"
	"time"

	"github.com/gorilla/websocket"
)

type WsMsg struct {
	Type    string `json:"type"`
	Payload string `json:"payload"`
}

var colorMap = map[string]string{
	"$BLK$": "\x1b[0;30m",
	"$RED$": "\x1b[0;31m",
	"$GRN$": "\x1b[0;32m",
	"$YEL$": "\x1b[0;33m",
	"$BLU$": "\x1b[0;34m",
	"$MAG$": "\x1b[0;35m",
	"$CYN$": "\x1b[0;36m",
	"$WHT$": "\x1b[0;37m",
	"$HIK$": "\x1b[1;30m",
	"$HIR$": "\x1b[1;31m",
	"$HIG$": "\x1b[1;32m",
	"$HIY$": "\x1b[1;33m",
	"$HIB$": "\x1b[1;34m",
	"$HIM$": "\x1b[1;35m",
	"$HIC$": "\x1b[1;36m",
	"$HIW$": "\x1b[1;37m",
	"$NOR$": "\x1b[0m",
}

func toAnsi(text string) string {
	for k, v := range colorMap {
		text = strings.ReplaceAll(text, k, v)
	}
	return text
}

func main() {
	// 1. 啟動 bin/fsmud 伺服器
	log.Println("🚀 正在啟動 fsmud 伺服器進行整合測試...")
	cmd := exec.Command("./bin/fsmud", "-mudlib", "fsmud", "-master", "master.c")

	// 捕獲輸出以追蹤任何運行期錯誤
	stdout, _ := cmd.StdoutPipe()
	cmd.Stderr = os.Stderr

	if err := cmd.Start(); err != nil {
		log.Fatalf("❌ 無法啟動伺服器: %v", err)
	}

	// 非同步讀取伺服器日誌
	go func() {
		scanner := bufio.NewScanner(stdout)
		for scanner.Scan() {
			line := scanner.Text()
			if strings.Contains(line, "RUNTIME ERROR") || strings.Contains(line, "panic") {
				fmt.Printf("\n🔥 [SERVER ERROR]: %s\n", line)
			}
		}
	}()

	// 確保結束時伺服器進程被終止
	defer func() {
		log.Println("🛑 正在關閉伺服器...")
		cmd.Process.Kill()
	}()

	// 2. 等待伺服器就緒
	time.Sleep(3 * time.Second)

	// 3. 連線至 fsmud 伺服器
	log.Println("🔌 正在連線至 fsmud 伺服器 (ws://localhost:8080/ws)...")
	u := url.URL{Scheme: "ws", Host: "localhost:8080", Path: "/ws"}
	conn, _, err := websocket.DefaultDialer.Dial(u.String(), nil)
	if err != nil {
		log.Fatalf("❌ 連線失敗: %v\n請確認 8080 埠未被佔用。", err)
	}
	defer conn.Close()
	log.Println("✅ 連線成功！")

	received := make(chan string, 100)
	go func() {
		for {
			_, message, err := conn.ReadMessage()
			if err != nil {
				log.Println("\n❌ 與伺服器連線中斷。")
				return
			}
			var msg WsMsg
			if err := json.Unmarshal(message, &msg); err == nil {
				if msg.Type == "mud_text" || msg.Type == "chat" {
					fmt.Print(toAnsi(msg.Payload))
					received <- msg.Payload
				}
			}
		}
	}()

	sendMsg := func(text string) {
		payload, _ := json.Marshal(WsMsg{Type: "cmd", Payload: text})
		conn.WriteMessage(websocket.TextMessage, payload)
	}

	// 4. 模擬自動登入程序
	time.Sleep(500 * time.Millisecond)
	
	log.Println("\n🤖 [自動測試] 選擇語系：2 (繁體中文)")
	sendMsg("2")
	time.Sleep(800 * time.Millisecond)

	log.Println("🤖 [自動測試] 輸入帳號：wade")
	sendMsg("wade")
	time.Sleep(800 * time.Millisecond)

	log.Println("🤖 [自動測試] 輸入密碼：jj")
	sendMsg("jj")
	time.Sleep(3500 * time.Millisecond)

	// 執行測試指令清單
	testCmds := []string{
		"ls",
		"pwd",
		"look",
		"out",
		"lm",
		"look",
		"mc leave", // 💡 測試完畢，離開創界世界，回到預設的新手村 (room_0_0)
		"shutdown",  // 💡 執行系統關閉指令，使伺服器存檔並安全退場
	}

	for _, cmdStr := range testCmds {
		log.Printf("\n🤖 [自動測試] 執行指令：%s", cmdStr)
		sendMsg(cmdStr)
		time.Sleep(1500 * time.Millisecond) // 等待伺服器回應與看清輸出
	}

	log.Println("\n🎉 [自動測試] 一鍵啟動 → 測試 → 關閉 整合測試執行完畢。")
}
