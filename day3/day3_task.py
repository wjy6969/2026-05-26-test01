def 统计关键词(文件路径, 关键词):
    """读取日志文件，统计关键词出现次数"""
    try:
        with open(文件路径, "r", encoding="utf-8") as f:
            内容 = f.read()
        次数 = 内容.count(关键词)
        return 次数
    except FileNotFoundError:
        print(f"⚠️ 文件不存在：{文件路径}")
        return 0

# 调用
日志路径 = r"D:\learn\learning\day3\day3.txt"
数据库次数 = 统计关键词(日志路径, "数据库")
培训次数 = 统计关键词(日志路径, "培训")
不存在次数 = 统计关键词(r"D:\learn\learning\day3\不存在.txt", "测试")

print(f"日志中『数据库』出现 {数据库次数} 次")
print(f"日志中『培训』出现 {培训次数} 次")
print(f"不存在文件的统计：{不存在次数}")