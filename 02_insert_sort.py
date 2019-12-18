"""
   插入排序---类似打麻将
   最好情况的时间复杂度是 O(n)，有序数组从第二个开始排序只会比较一次
   平均和最坏情况的时间复杂度是 O(n2)
   空间复杂度O(n)
"""
def insert_sort(array):
    lens = len(array)
    # 从第2个元素开始插入排序
    for i in range(1, lens):
        cur_num = array[i]

        # 从i索引开始往前逐个比较
        for j in range(i-1, -1, -1):
            # 如果前一个数比当前数大，则前一个数放到当前位置
            if array[j] > cur_num:
                array[j+1] = array[j]
                array[j] = cur_num  # 这一步可不要忘了
            else:
                break  # 若前一个数小，则退出当前for循环


# Test
arr = [4, 7 ,28 ,2 , 13 , 5, 1, 12, 1]
insert_sort(arr)
print(arr)
