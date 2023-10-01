import numpy as np
arr1 = input("")
num1 = [int(n) for n in arr1.split()] 
print("数组A:", num1)
num2 = np.ones(len(num1))
for i in range(len(num1)):
    for j in range(len(num1)):
        if(i != j):
            num2[i]=num2[i]*num1[j]
print("数组B:",num2)