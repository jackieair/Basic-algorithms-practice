class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #  regular expression：re
        if not s and not p:
            return True  # 两个字符串都为空，返回true
        elif s and not p:
            return False  # s空匹配s不空一定错误
        elif not s and p:
            # s空 匹配p不空则要分情况讨论
            if len(p) > 1 and p[1] == '*':
                return self.isMatch(s, p[2:])  # 如果匹配p[1]为'*',则p前2为可以匹配为空，继续比较后续
            else:
                return False
        # s与p都不空的情况下
        else:
            # p[1] = '*'的情况下
            if len(p) > 1 and p[1] == '*':
                if s[0] != p[0] and p[0] != '.':
                    return self.isMatch(s, p[2:])  # 如果s，p首字符不匹配且p[0] != '.', 则置为空继续比较
                else:
                    # 否则就是比较3种情况：1-p前2位当空，2-；3-
                    return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p[2:]) or self.isMatch(s[1:], p)

            else:
                # p[1] !='*'的情况下
                if s[0] == p[0] or p[0] == '.':
                    return self.isMatch(s[1:], p[1:])

                else:
                    return False

a = Solution()
print(a.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
