def binary_search(list, item):
    """二分法算法实现"""
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left + right)
        if list[mid] == item:
            return mid

        if list[mid] > item:
            right = mid -1
        else:
            left = mid + 1

    print("No result found!")

list = [1, 2, 33, 43, 232, 545, 548, 613, 624, 723, 843, 902, 1023, 1256, 1467, 1899, 2048]
item = 1222

print(binary_search(list, item))
