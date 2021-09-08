'''
每日一题 8.30
528.按权重随机选择
'''
from typing import List
import random

class Solution:

    def __init__(self, w: List[int]):
        # 前缀和
        self.preSum = w
        for i in range(1, len(w)):
            self.preSum[i] += w[i - 1]

    def pickIndex(self) -> int:
        rand = random.randint(1, self.preSum[-1])
        for i in range(len(self.preSum)):
            if rand <= self.preSum[i]:
                return i

        return 0

w = [3, 1, 2, 4]
# preSum = [3, 4, 6, 10]
# [3, 3, 3, 1, 2, 2, 4, 4, 4, 4]
solve = Solution(w)
print(solve.pickIndex())
