import time
def bubble_sort(list):
    """
    实现冒泡排序算法：
    从左到右，数组中相邻的两个元素进行比较，将较大的放到后面。
    相比于选择排序，每次比较可能都要交换，效率低
    """
    for i in range(len(list)):

        #由于排一次，最后一个元素为max，故跳过比较-->len(list)-1-i
        for j in range(len(list)-1-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

    return list


array = [8, 3, 10, 7, 0, 10, 2, 156, 141, 35, 4, 88, 4, 61, 111]
start_time = time.time()

time.sleep(2)
bubble_sort(array)

period = time.time() - start_time
print(period)
print(array)
