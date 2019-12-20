"""
   插入排序---升级版
   插入排序一次只能将数据移动一位，而希尔排序加入gap实现跳跃移动
   当gap为1时，等同于插入排序
   最好时间复杂度O(n),平均最差时间复杂度O((nlog(n))^2)，空间复杂度O(1)
"""
def shell_sort(array):
    lens = len(array)
    gap = 1

    while gap < lens:
        gap = gap * 3 + 1  # 区间通俗取法

    while gap > 0:
        for i in range(1, lens):
            cur_num = array[i]
            j = i - gap
            while j >= 0 and arr[j] > cur_num:
                # 只要满足当前值比cur_num大，就把当前值移动到后面一个位置
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = cur_num

        gap = gap // 3


# Test
arr = [4, 1, 11, 7, 8, 2, 3, 5, 24, 5, 43, 22, 19]
hill_sort(arr)
print(arr)
