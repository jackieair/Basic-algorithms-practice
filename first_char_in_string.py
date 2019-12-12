class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        hash_map = dict()
        for i in range(0, len(s)):
            if hash_map[s[i]] >= 1:
                hash_map[s[i]] += 1
            else:
                hash_map[s[i]] = 1

        for i in range(0, len(s)):
            if hash_map[s[i]] == 1:
                return i
        return -1

t = dict()

print(ord('A'))
print(chr(97))
