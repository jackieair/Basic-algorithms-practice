"""
    计数排序时间复杂度为O(n+m),空间复杂度O(n)
    m为数据量
    局限性在于如果排的数据范围比较大但是数据量比较小，如[1,999]比较2个数创建999个数组显然不实际
    计数排序只适用于正整数并且取值范围相差不大的数组排序使用，它的排序的速度是非常可观的。
"""

def count_Sort(arr):
    # 找出数组最大数
    max_num = max(arr)

    # 初始化计数数组
    count_arr = [0 for _ in range(max_num+1)]

    # 计数
    for num in arr:
        count_arr[num] += 1

    # 排序
    index = 0
    for i in range(max_num+1):
        while count_arr[i] > 0:
            arr[index] = i
            index += 1
            count_arr[i] -= 1

    return arr


# 测试用例
arr = [6, 11, 11, 22, 5, 6, 7, 3, 3]
count_Sort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
    print ("{}".format(arr[i]))





