"""插入排序---类似打麻将"""
def insert_sort(array):
    lens = len(array)
    # 从第2个元素开始插入排序
    for i in range(1, lens):
        cur_num = array[i]
        # 从i索引开始往前逐个比较
        for j in range(i, -1, -1):
            # 如果前一个数比当前数大，则前一个数放到当前位置
            if array[j-1] > cur_num:
                array[j] = array[j-1]
            else:
                break # 若前一个数小，则退出当前for循环
        array[j] = cur_num


# Test
arr = [4, 7 ,8 ,2 ,3 ,5]
insert_sort(arr)
print(arr)
