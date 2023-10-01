"""
求最大公约数
"""
def gcd(a, b):
    while b!=0:
        a, b = b, a % b
    return a

# 输入两个整数
num1 = int(input("请输入第一个整数: "))
num2 = int(input("请输入第二个整数: "))

# 计算它们的最大公约数
result = gcd(num1, num2)

print(f"{num1} 和 {num2} 的最大公约数是 {result}")
