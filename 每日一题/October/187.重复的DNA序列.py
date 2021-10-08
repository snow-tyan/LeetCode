'''
10.8 每日一题
187.重复的DNA序列
'''
from typing import List
import collections


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        mp = collections.Counter()
        res = []
        for i in range(n - 10 + 1):
            sub = s[i:i + 10]
            mp[sub] += 1
            if mp[sub] == 2:
                res.append(sub)
        return res


solve = Solution()
# s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
s = "AAAAAAAAAAA"
print(solve.findRepeatedDnaSequences(s))
