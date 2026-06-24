#backend
DATE   := $(shell date +%Y%m%d)
USER := $(shell whoami)

COMMIT := $(shell git rev-parse --short=8 HEAD)
VERSION := $(COMMIT)-$(DATE)

TOP=$(shell pwd)
OUT=$(TOP)/bin

# 🚀 智慧路徑偵測：優先使用系統環境，找不到才用預設值
DETECTED_GOROOT := $(shell go env GOROOT 2>/dev/null)
GOROOT ?= $(DETECTED_GOROOT)
ifeq ($(GOROOT),)
    GOROOT := /usr/local/go-1.26.2
endif

# 🚀 根據 GOROOT 是否存在來決定 Go 執行檔路徑
GO_EXE := $(shell if [ -f $(GOROOT)/bin/go ]; then echo $(GOROOT)/bin/go; else echo go; fi)

# 環境變數配置 (移除強制 GOROOT 以相容 CI)
GO_FLAGS := -ldflags="-s -w"
COMMON_ENV := CGO_CFLAGS="-Wno-return-local-addr"
ENVW := $(COMMON_ENV) CGO_ENABLED=1 GOOS=windows GOARCH=amd64 CC="x86_64-w64-mingw32-gcc -fno-stack-protector -D_FORTIFY_SOURCE=0 -lssp"

.PHONY: all clean test test-driver test-fsmud fsmud fsmud.exe run-fsmud

all: fsmud fsmud.exe

clean-txt:
	@ rm -f *txt *log

$(OUT):
	@mkdir -p $(OUT)

# 編譯 Linux 版本
fsmud: $(OUT)
	@echo "🔨 Building $@ (Linux Standard)..."
	@go mod tidy && $(COMMON_ENV) $(GO_EXE) build $(GO_FLAGS) -tags fsmud -o $(OUT)/$@ ./cmd/fsmud
	@ls -l $(OUT)/$@

# 編譯 Windows 版本 (.exe)
fsmud.exe: $(OUT)
	@echo "🔨 Building $@ (Windows Standard)..."
	@go mod tidy && $(ENVW) $(GO_EXE) build $(GO_FLAGS) -tags fsmud -o $(OUT)/$@ ./cmd/fsmud
	@ls -l $(OUT)/$@

# 執行測試
test-driver: mudscript
	@echo "🧪 Running MudScript Core Tests on driver in isolation..."
	@MUD_TEST_MODE=1 $(OUT)/mudscript -mudlib testlib -master master.c --hub none 2>&1 | tee test-driver.txt

test: test-driver

# 正常執行伺服器
run-fsmud: fsmud
	@echo "🚀 Starting MudScript Server (Connecting to Global Hub)..."
	@ ./bin/fsmud -mudlib fsmud -master master.c 2>&1 | tee run-fsmud.txt

# 執行 FSMUD 自動化一鍵整合測試
test-fsmud: fsmud
	@echo "🧪 Running Integration Test on FSMUD..."
	@go run ./cmd/test-fsmud/main.go


clean:
	@rm -rf *.log *txt $(OUT)/*
