# Day 3 学习笔记 日期：2026-07-03

## 学习内容
with open 文件读取 / try-except 异常处理 / encoding 编码 / r-string 原始字符串 / 函数定义与调用

## 产出文件
- day3_task.py — 统计日志中关键词出现次数
- day3.txt — 测试日志数据
- test.py — 实验验证（f 类型、读文件流程）

## 遇到的坑
- PowerShell 5.1 默认 GBK 读 UTF-8 文件会乱码（后来换 PowerShell 7 解决）
- FileNotFoundError 被 except 静默吞掉，调用方感知不到（设计需改进）
- raw string r"..." 处理 Windows 路径里的反斜杠

## 新掌握的命令
- with open(..., "r", encoding="utf-8") as f:  — 安全读文件
- try / except FileNotFoundError / return — 兜底异常
- f.read() / f"格式化字符串" / r"原始字符串"