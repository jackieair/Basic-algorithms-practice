def select_sort(list):
    """
    实现选择排序算法---》不稳定排序
    从第一个位置开始比较，找出最小的，和第一个位置互换，开始下一轮。
    """
    for i in range(len(list)):
        min_idx = i  # 外循环最小值索引
        """开始 n x n 循环"""
        for j in range(i+1, len(list)):
            if list[j] < list[min_idx]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]

    return list

play_number = [156,141,35,4,88,61,111]
print(select_sort(play_number))

