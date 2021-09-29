'''
9.29 每日一题
517.超级洗衣机
'''
from typing import List


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        n = len(machines)
        if total % n != 0:
            return -1
        res = 0
        max_cloth = max(machines)
        avg = total // n  # 最终每个洗衣机衣服
        pre_sum = 0  # 前i个洗衣机衣服总和pre_sum
        # 每次只能往相邻洗衣机移动一件衣服 则
        # 对最多衣服的洗衣机需要max_cloth-avg次移动
        # 对前i个洗衣机至少需要abs(pre_sum-i*avg)次移动
        for i in range(n):
            pre_sum += machines[i]
            res = max(res, max(max_cloth - avg, abs(pre_sum - (i + 1) * avg)))
        return res
