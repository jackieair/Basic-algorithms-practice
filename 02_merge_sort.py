"""归并排序核心思想---分而治之
   merge合并时间复杂度为O(N),分解数组对半切割时间复杂度为O(logn),;
   总的时间为O(nlogn)=logN层
   空间复杂度O(n)
"""

def merge_sort(arr):
    lens = len(arr)
    if lens <= 1:
        return arr

    mid = lens // 2
    left = arr[:mid]
    right = arr[mid:]

    l_arr = merge_sort(left)
    r_arr = merge_sort(right)

    return merge(l_arr, r_arr)

def merge(l_arr, r_arr):
    arr = []
    l_idx = 0
    r_idx = 0

    while l_idx < len(l_arr) and r_idx < len(r_arr):
        if l_arr[l_idx] <= r_arr[r_idx]:
            arr.append(l_arr[l_idx])
            l_idx += 1
        else:
            arr.append(r_arr[r_idx])
            r_idx += 1

    if len(l_arr[l_idx:]) > 0:
        arr = arr + l_arr[l_idx:]
    if len(r_arr[r_idx:]) > 0:
        arr = arr + r_arr[r_idx:]

    return arr

print(merge_sort([8,3,1,7,0,10,2]))
