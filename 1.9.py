arr = input("请随机输入一个序列：")
num = [int(n) for n in arr.split()]
len = len(num)
print("for循环的结果：",end="")
for i in range(1,len+1):
    print(num[len-i],end=" ")
j=1
print("\nwhile循环的结果：",end="")
while j<=len:
    print(num[len-j],end=" ")
    j=j+1



