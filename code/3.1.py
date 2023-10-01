def conFra(n):
    x='0.'
    while(n!=0):
        n=n*2
        x+=str(int(n))
        n=n-int(n)
    print(x)
num=float(input("请输入小数："))
print("该小数的二进制为：")
conFra(num)