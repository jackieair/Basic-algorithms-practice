"""
    快速排序--》不稳定，空间复杂度logn
    平均最好时间复杂度O(nlogn),最差O(n2)
"""

import time
def per_pivot_sort(arr, low, high):
    """
    调用该函数返回一次快速排序后的pivot索引，分而治之"""
    left_idx = low
    pivot_idx = high

    while left_idx != pivot_idx:
        if arr[left_idx] <= arr[pivot_idx]:
            left_idx += 1
        else:
            # 代码太长，可以用反斜杠链接‘\’
            arr[left_idx], arr[pivot_idx-1], arr[pivot_idx] = arr[pivot_idx-1], arr[pivot_idx], arr[left_idx]
            pivot_idx -= 1

    return pivot_idx


def quick_sort(arr, low, high):
    """快排主函数"""
    # 基线条件
    if low > high:
        return

    mid = per_pivot_sort(arr, low, high)

    #分而治之
    quick_sort(arr, low, mid-1)
    quick_sort(arr, mid+1, high)

    return arr


# 测试用例

array = [8, 3, 10, 7, 0, 10, 2, 156, 141, 35, 4, 88, 4, 61, 111]
start_time = time.time()

time.sleep(1)
quick_sort(array, 0, len(array)-1)

period = time.time() - start_time
print(period)
print(array)
