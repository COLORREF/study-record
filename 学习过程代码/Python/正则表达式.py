import re  # 导入正则表达式模块

# 参数1：匹配规则
# 参数2：数据来源


# . 任意一个字符处理\n
# [ ] 匹配中括号中列举的字符
# \d 匹配数字 0-9
# \D 匹配非数字，即不是数字
# \s 匹配空白和制表符（\t）
# \S 匹配非空白
# \w 匹配非特殊字符，即a-z、A-Z、0-9、_、汉字
# \W 匹配特殊字符，即非字母、非数字、非汉字

ret = re.match()

info = ret.group()
print(info)
