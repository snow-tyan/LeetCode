'''
10.1 每日一题
1436.旅行终点站
'''
from typing import List
import collections

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # 终点必是没有出度的节点
        cnt = collections.Counter()
        for src, des in paths:
            cnt[src] -= 1  # 出度
            cnt[des] += 1  # 入度
        for key, val in cnt.items():
            if val == 1:
                return key
        return ''


solve = Solution()
print(solve.destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
