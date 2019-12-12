class Solution:
    def __init__(self,data):
        self.data = data

    def InversePairs(self):
        # write code here
        data = self.data
        new_data, count = self.mergesort(data)
        return count % 1000000007

        # 归并排序

    def mergesort(self, data):
        lens = len(data)
        if lens <= 1:
            return data, 0

        mid = lens // 2
        left = data[:mid]
        right = data[mid:]

        l_data, l_count = self.mergesort(left)
        r_data, r_count = self.mergesort(right)

        total_count = l_count + r_count
        data, tol = self.merge(l_data, r_data)

        count = tol + total_count
        return data, count

    def merge(self, l_data, r_data):
        new_list = []
        l_idx, r_idx = 0, 0
        count = 0

        while l_idx < len(l_data) and r_idx < len(r_data):
            if l_data[l_idx] > r_data[r_idx]:
                new_list.append(r_data[r_idx])
                r_idx += 1
                # 现在的data都已经是排好序的，故左边i_idx及后边的都大于右边
                l_data_remain = len(l_data) - l_idx
                count += l_data_remain
            else:
                new_list.append(l_data[l_idx])
                l_idx += 1

        if len(l_data[l_idx:]) > 0:
            new_list += l_data[l_idx:]
        if len(r_data[r_idx:]) > 0:
            new_list += r_data[r_idx:]

        return new_list, count

s = Solution([8,3,1,7,0,10,2])
print(s.InversePairs())
