"""插入排序---升级版"""
def hill_sort(array):
    lens = len(array)
    gap = 1

    while gap < lens:
        gap = gap * 3 + 1  # 区间通俗取法

    while gap > 0:
        for i in range(1, lens):
            cur_num = array[i]
            j = i - gap
            while j >= 0 and arr[j] > cur_num:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = cur_num

        gap = gap // 3


# Test
arr = [4, 1, 11, 7 ,8 ,2 ,3 ,5]
hill_sort(arr)
print(arr)
