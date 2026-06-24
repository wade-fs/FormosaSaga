//go:build fs && !fsmud && !universal
// +build fs,!fsmud,!universal

package mudscript

import "embed"

// 🚀 專供給 fs 輕量版使用的資源
//go:embed all:fs
var Assets embed.FS
