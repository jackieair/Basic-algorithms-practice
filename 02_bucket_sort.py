"""
   python之桶排序，算是计数排序的改进
   几个数就设置几个桶比较合理，关键是求得区间长度
   利用数除以区间长度取整数作为桶的索引
   最佳及平均时间复杂度为O(n+k),最差为O(n^2);空间复杂度O(n)
"""
def bucket_Sort(array):
    length = len(array)
    buckets = [[] for _ in range(length)]  # 设置桶的个数

    # 找出最大最小值确定后续划分区间
    max_num = max(array)
    min_num = min(array)
    diff = max_num - min_num

    # 知道长度和差值，即可确定区间长度
    section = diff // length + 1  # 加1是关键，关键，关键

    # 数据入桶
    for num in array:
        idx = num // section
        buckets[idx].append(num)
    # 桶内排序
    for arr in buckets:
        # 一个桶有2个数及以上需要考虑排序
        if len(arr) > 1:
            arr.sort()  # 插入排序

    # 写入原数组
    index = 0
    for arr in buckets:
        if arr:
            for j in range(len(arr)):
                array[index] = arr[j]
                index += 1
    return array

# 测试用例
arr = [6, 11, 11, 22, 5, 6, 7, 3, 3, 23, 333, 43]
bucket_Sort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
    print ("{}".format(arr[i]))



