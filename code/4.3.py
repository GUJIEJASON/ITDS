"""
直接插入排序
"""
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # 当前要插入的元素
        j = i - 1

        # 将比key大的元素向右移动，为key腾出位置
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # 插入key到正确的位置
        arr[j + 1] = key

# 测试插入排序
arr = input("") #输入一个一维数组，每个数之间使空格隔开
num = [int(n) for n in arr.split()] #将输入每个数以空格键隔开做成数组
print("原始数组:", num)
insertion_sort(num)
print("排序后的数组:", num)
