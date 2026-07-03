Day 2 学习笔记
日期：2026-07-02

学习内容
变量与数据类型
if/elif/else 条件判断
for 循环 + zip 联动遍历
f-string 格式化字符串
实战任务
批量数据库巡检脚本：遍历 3 个客户库，根据状态码判断连接是否正常。

产出
文件	说明
day2_task.py	批量巡检脚本（变量/if/for/zip/f-string）
遇到的坑
PowerShell Here-String 空行 + 回车触发执行
Move-Item 不能在当前目录下移动自己
git add . 空格被 PowerShell 自动补全吃掉
新掌握的命令
命令	            作用
Move-Item	        移动文件/文件夹
Get-Content	        读取文件内容
ni (New-Item)	    新建文件