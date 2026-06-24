package main

import (
	"fmt"
	"log"
	"net"
	"time"

	"github.com/pion/stun"
)

func main() {
	fmt.Println("🔍 開始診斷 NAT 類型...")

	// 1. 建立一個本地的 UDP Socket (系統會自動分配一個隨機的 Port)
	localAddr, err := net.ResolveUDPAddr("udp4", "0.0.0.0:0")
	if err != nil {
		log.Fatal(err)
	}
	conn, err := net.ListenUDP("udp4", localAddr)
	if err != nil {
		log.Fatal(err)
	}
	defer conn.Close()

	fmt.Printf("📍 本地綁定的 UDP Port: %d\n\n", conn.LocalAddr().(*net.UDPAddr).Port)

	// 定義兩個不同的 STUN 伺服器
	server1 := "stun.l.google.com:19302"
	server2 := "global.stun.twilio.com:3478"

	// 2. 測試第一個 STUN 伺服器
	addr1, err := testSTUN(conn, server1)
	if err != nil {
		log.Fatalf("連線 %s 失敗: %v", server1, err)
	}
	fmt.Printf("🌐 透過 %s 取得的公網位址: %s\n", server1, addr1.String())

	// 3. 測試第二個 STUN 伺服器
	addr2, err := testSTUN(conn, server2)
	if err != nil {
		log.Fatalf("連線 %s 失敗: %v", server2, err)
	}
	fmt.Printf("🌐 透過 %s 取得的公網位址: %s\n", server2, addr2.String())

	// 4. 比較結果
	fmt.Println("\n--- 🏁 診斷結果 ---")
	if addr1.Port == addr2.Port {
		fmt.Println("🟢 恭喜！您的網路不是 Symmetric NAT (通常是 Cone NAT)。")
		fmt.Println("👉 WebRTC P2P 可以輕鬆穿透，不需要 TURN 伺服器！")
	} else {
		fmt.Println("🔴 警告：您的網路是 Symmetric NAT (對稱型 NAT)！")
		fmt.Println("👉 因為連到不同伺服器時，您的 NAT 分配了不同的 Port。")
		fmt.Println("👉 在這種網路下，P2P 連線極高機率會失敗，必須依賴 TURN 伺服器中繼。")
	}
}

// testSTUN 發送 STUN Request 並回傳解析出的公網 IP 與 Port
func testSTUN(conn *net.UDPConn, serverAddr string) (*net.UDPAddr, error) {
	// 解析 STUN 伺服器 IP
	dstAddr, err := net.ResolveUDPAddr("udp4", serverAddr)
	if err != nil {
		return nil, err
	}

	// 建立 STUN Binding Request 訊息
	msg := stun.MustBuild(stun.TransactionID, stun.BindingRequest)

	// 從我們綁定的本地 UDP Socket 送出封包
	_, err = conn.WriteToUDP(msg.Raw, dstAddr)
	if err != nil {
		return nil, err
	}

	// 設定讀取超時 (3秒)
	conn.SetReadDeadline(time.Now().Add(3 * time.Second))

	// 接收回應
	buf := make([]byte, 1024)
	n, _, err := conn.ReadFromUDP(buf)
	if err != nil {
		return nil, err
	}

	// 解析 STUN 回應
	res := new(stun.Message)
	res.Raw = buf[:n]
	if err := res.Decode(); err != nil {
		return nil, err
	}

	// 取得映射的公網位址 (優先抓取 XOR-MAPPED-ADDRESS)
	var xorAddr stun.XORMappedAddress
	if err := xorAddr.GetFrom(res); err == nil {
		return &net.UDPAddr{IP: xorAddr.IP, Port: xorAddr.Port}, nil
	}

	// 備用：有些舊伺服器只回 MAPPED-ADDRESS
	var mappedAddr stun.MappedAddress
	if err := mappedAddr.GetFrom(res); err == nil {
		return &net.UDPAddr{IP: mappedAddr.IP, Port: mappedAddr.Port}, nil
	}

	return nil, fmt.Errorf("無法從 STUN 回應中找到 Mapped Address")
}
