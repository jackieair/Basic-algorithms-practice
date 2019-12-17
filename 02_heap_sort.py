"""
   堆排序，分为建堆和堆化2个过程
   时间复杂度O(nlogn），空间复杂度O(1)
   建堆时间复杂度为O(n),堆调整O(nlogn)!!
   堆排序的时间复杂度为nlogn,构建堆的时间复杂度为o(n),重建堆的时间复杂度为nlogn.
"""

def heapfy(arr, n, i):
    # n为堆的尺寸
    largest = i
    # 左右子节点
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        # 如果左子节点存在且大于当前根节点，交换
        largest = l

    if r < n and arr[largest] < arr[r]:
        # 若右子节点存在且大于当前跟节点，交换
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 如果存在要交换的点，则交换
        # 堆化根节点
        heapfy(arr, n, largest)


def heapSort(arr):
    # 堆排序主程序
    n = len(arr)

    # 建立最大堆
    for i in range(n, -1, -1):
        heapfy(arr, n, i)

    # 逐个提取元素
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        heapfy(arr, i, 0)

    return


# 测试用例
# Driver code to test above
arr = [ 12, 11, 13, 5, 6, 7, 89, 23, 11, 3, 5, 66, 12]
heapSort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
    print ("{}".format(arr[i]))
