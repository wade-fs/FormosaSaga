# 1. Build Stage
FROM golang:1.26-alpine AS builder

WORKDIR /app

# 安裝編譯所需的工具 (如果有的話)
RUN apk add --no-cache make git

# 複製依賴文件
COPY go.mod go.sum ./
RUN go mod download

# 複製源碼
COPY . .

# 編譯 Linux 版本
RUN make fsmud

# 2. Final Stage
FROM alpine:latest

WORKDIR /app

# 安裝運行時必要的套件
RUN apk add --no-cache libc6-compat ca-certificates

# 從 Build Stage 複製編譯好的執行檔與必要資源
COPY --from=builder /app/bin/fsmud /app/fsmud
COPY --from=builder /app/mudlib /app/mudlib
COPY --from=builder /app/web /app/web

# Hugging Face Spaces 預設會使用 7860 連接埠
EXPOSE 7860

# 啟動指令：作為 Hub 執行，並監聽 7860
CMD ["./fsmud", "--port", "7860"]
