num=int(input("请输入一个自然数:"))
def factorial(num):
    sum=1
    i=1
    while(i<=num):
        sum=sum*i
        i=i+1
    print(num,"的阶乘是：",sum)
factorial(num)
    