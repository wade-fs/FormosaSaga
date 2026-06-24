//go:build universal || (fs && fsmud)
// +build universal fs,fsmud

package mudscript

import "embed"

// 🚀 旗艦全能版資源：同時內嵌兩個世界
//go:embed all:fsmud all:fs
var Assets embed.FS
