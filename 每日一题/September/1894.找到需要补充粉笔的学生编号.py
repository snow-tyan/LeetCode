'''
1894.找到需要补充粉笔的学生编号
'''
from typing import List


class Solution:
    # 暴力 TLE
    def chalkReplacerBL(self, chalk: List[int], k: int) -> int:
        while True:
            for i, c in enumerate(chalk):
                k -= c
                if k <= 0:
                    return i

    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # 前缀和 preSum[i] 为前i-1个数之和,第一个位置不存
        n = len(chalk)
        preSum = [0]
        for i in range(n):
            preSum.append(preSum[i] + chalk[i])
        k %= preSum[n]
        for i in range(1, n + 1):
            if preSum[i] > k:
                return i - 1

    # 模拟
    def chalkReplacerMO(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        # print(k)
        for i, c in enumerate(chalk):
            k -= c
            if k < 0:
                return i
