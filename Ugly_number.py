def GetUglyNumber_Solution(index):
    # write code here
    if index < 7:
        return index # 若数字小于7，则全都是丑数

    rsl = [None for _ in range(index)]
    rsl[0] = 1
    t2, t3, t5 = 0, 0, 0
    i = 1
    while i < index:
        rsl[i] = min(rsl[t2] * 2, min(rsl[t3] * 3, rsl[t5] * 5))
        if rsl[i] == rsl[t2] * 2:
            t2 += 1
        if rsl[i] == rsl[t3] * 3:
            t3 += 1
        if rsl[i] == rsl[t5] * 5:
            t5 += 1
        i += 1
    return rsl[index-1]

print(GetUglyNumber_Solution(88))
