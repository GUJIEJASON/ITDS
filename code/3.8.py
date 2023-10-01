import random
def random_list(n):
    # 生成包含10个随机整数的列表（范围在0到100之间）
    random_list = [random.randint(0, 100) for i in range(n)]
    # 打印随机数列
    print(random_list)
    return random_list

def selection_sort(arr):
    # 遍历整个数组
    for i in range(len(arr)):
        # 假设当前索引的元素是最小的
        min_index = i
        
        # 在未排序的部分中找到最小的元素的索引
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # 将找到的最小元素与当前位置交换
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)
def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1
 
    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)
 
    return c
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr)//2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)
length=[]
length=random_list(5)
num1=random_list(length[0])
num2=random_list(length[1])
num3=random_list(length[2])
num4=random_list(length[3])
num5=random_list(length[4])
num6=num1.copy()
num7=num2.copy()
num8=num3.copy()
num9=num4.copy()
num10=num5.copy()

print("选择排序的结果：")
selection_sort(num1)
selection_sort(num2)
selection_sort(num3)
selection_sort(num4)
selection_sort(num5)
print("归并排序的结果：")
print(merge_sort(num6))
print(merge_sort(num7))
print(merge_sort(num8))
print(merge_sort(num9))
print(merge_sort(num10))
