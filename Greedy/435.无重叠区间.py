'''
435.无重叠区间
452.用最少数量的箭引爆气球
'''
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # [start, end] 默认start<end
        # 把intervals按end排序，选择end最小的区间
        # 遍历intervals，下一个区间start>当前end，则无重叠
        res = 0
        # print(intervals)
        intervals.sort(key=lambda x: x[1])
        # print(intervals)
        _, end = intervals[0]
        for i in range(1, len(intervals)):
            # 下一个数的start必须>=上一个数的end
            if intervals[i][0] < end:
                res += 1
            else:
                end = intervals[i][1]  # 更新end
        return res

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        count = 1
        points.sort(key=lambda x: x[1])
        _, end = points[0]
        for i in range(1, len(points)):
            if points[i][0] > end:  # 擦边也会被一支箭射爆
                count += 1
                end = points[i][1]
        return count


solve = Solution()
intervals = [[1, 2], [1, 2], [1, 2]]
print(solve.eraseOverlapIntervals(intervals))
points = [[1, 2], [2, 3], [3, 4], [4, 5]]
print(solve.findMinArrowShots(intervals))
print(solve.findMinArrowShots(points))
