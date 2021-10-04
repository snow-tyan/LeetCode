'''
第261场周赛
A.转换字符串的最少操作次数
B.找出缺失的观测数据
C.石子游戏IX
D.含特定字母的最小序列
'''
from typing import List


class Solution:
    def minimumMoves(self, s: str) -> int:
        # for循环改变i 不能修改循环次数
        res = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] == 'X':
                res += 1
                i += 2
            i += 1
        return res
