"""
希尔排序
"""
def ShellSort(nums):
    step = len(nums)//2 #初始化增量为数组长度的一半
    while step > 0: #增量必须是大于0的整数
        for i in range(step,len(nums)): #遍历需要进行插入排序的数
            ind = i
            while ind >= step and nums[ind] < nums[ind-step]: #对每组进行插入排序
                nums[ind],nums[ind-step] = nums[ind-step],nums[ind]
                ind -= step
        step //= 2 #增量缩小一半
arr = input("") #输入一个一维数组，每个数之间使空格隔开
num = [int(n) for n in arr.split()] #将输入每个数以空格键隔开做成数组
print("原始数组:", num)
ShellSort(num)
print("排序后的数组:", num)