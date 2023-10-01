"""
判断是否为质数
"""
num= int(input('输入一个任意的大于1的整数:'))
for i in range(3,num):
    a = num%i
    if (a ==0):
        print(num,'不是质数')
        break
    if (i ==num-1):
        print(num,'是质数')