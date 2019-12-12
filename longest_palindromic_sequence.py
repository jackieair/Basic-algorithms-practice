def longestPalindrome(s):
        # 字符串长度
        n = len(s)
        if n <= 1: n

        matrix = [[0 for _ in range(n)] for _ in range(n)]  # 创建矩阵

        for i in range(n):
            matrix[i][i] = 1  # 对角线设置为1

        """ 对字符串进行长度为2~n的遍历"""
        for size in range(2, n+1):
            # 长度从2，3，4…n,同时每个长度字符串比较收尾是否相同
            for start in range(n-size+1):
                # 对于长度为n字符串，如果长度取为size，那么最后一个子序列只能从n-size开始
                end = size + start -1
                if s[start] == s[end]:
                    matrix[start][end] = matrix[start+1][end-1] + 2
                else:
                    matrix[start][end] = max(matrix[start][end-1], matrix[start+1][end])

        return matrix[0][-1]


print(longestPalindrome('abcdea'))
