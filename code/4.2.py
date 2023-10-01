"""
获取程序执行时间
"""
import time

# 记录开始时间
start_time = time.time()

# 要执行的程序，以4.1为例
num= int(input('输入一个任意的大于1的整数:'))
for i in range(3,num):
    a = num%i
    if (a ==0):
        print(num,'不是质数')
        break
    if (i ==num-1):
        print(num,'是质数')
        
# 记录结束时间
end_time = time.time()

# 计算执行时间（以秒为单位）
execution_time = end_time - start_time
print(f"程序执行时间: {execution_time} 秒")
