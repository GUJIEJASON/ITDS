S=input("请输入一个字符串:")
len=len(S)
sum=1
for i in range(len-1):
    if(S[i+1]==S[i]):
        sum=sum+1
    elif(S[i+1]!=S[i] and sum!=1):
        print(S,"中就包含",S[i]*sum,"这个由",sum,"个连续字符",S[i],"组成的字符串")
        sum=1
if(sum!=1):
    print(S,"中就包含",S[len-1]*sum,"这个由",sum,"个连续字符",S[len-1],"组成的字符串")