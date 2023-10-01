"""
用正则表达式验证身份证号码是否合法
"""
import re

def validate_id_card(id_card):
    # 定义身份证号码的正则表达式模式
    pattern = r'^[1-9]\d{5}(18|19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}(\d|X|x)$'

    # 使用正则表达式进行匹配
    if re.match(pattern, id_card):
        return True
    else:
        return False

# 测试示例
id_card = str(input("请输入一串身份证号码："))
if validate_id_card(id_card):
    print("身份证号码有效")
else:
    print("身份证号码无效")
