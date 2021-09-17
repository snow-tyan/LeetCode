'''
9.13 每日一题
447.回旋镖数量
'''

from typing import List
import collections


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        # 枚举回旋镖中点
        for p in points:
            cnt = collections.Counter()
            x1, y1 = p
            for q in points:
                x2, y2 = q
                dis = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)  # 乘法比乘方效率高
                cnt[dis] += 1

            for m in cnt.values():  # m个点取2个点 A_m^2 = m * (m - 1)
                res += m * (m - 1)
        return res
