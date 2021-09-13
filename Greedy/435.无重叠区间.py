'''
区间问题
435.无重叠区间
452.用最少数量的箭引爆气球
1024.视频拼接
1288.删除被覆盖区间
56.合并区间
986.区间列表的交集
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

    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # 因要拼成[0,T]视频，起点必含0
        # 排序：1 按左端点升序 2 按右端点降序
        n = len(clips)
        clips.sort(key=lambda x: (x[0], -x[1]))
        # print(clips)
        res = 1
        cur_s, cur_e = clips[0]
        if cur_s != 0:
            return -1
        if cur_e >= time:
            return res
        next_e = cur_e
        # 遍历clips
        i = 1
        while i < n and clips[i][0] <= cur_e:
            # 比较所有next_s<=cur_e<next_e的区间，选择next_e最大的区间作为下一个
            while i < n and clips[i][0] <= cur_e:
                next_e = max(next_e, clips[i][1])
                i += 1
            res += 1
            cur_e = next_e
            if cur_e >= time:
                return res

        return -1

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # 排序 1 左端点升序 2 右端点降序
        # 按这种方法排序，相邻区间只会出现三种情况 1 覆盖 2 交集 3 不相交
        # 只有覆盖才会出现 next_end<cur_end
        # 计数右端点大于cur_end的区间
        n = len(intervals)
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 1
        _, cur_e = intervals[0]
        for i in range(1, n):
            _, next_e = intervals[i]
            if next_e > cur_e:
                cur_e = next_e
                count += 1

        return count

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1 start升序 2 end降序
        # 相邻区间只有三种情况 1 覆盖 2 相交->可合并 3 不相交
        n = len(intervals)
        intervals.sort(key=lambda x: (x[0], -x[1]))
        # print(intervals)
        cur_start, cur_end = intervals[0]
        res = [intervals[0]]
        for i in range(1, n):
            next_start, next_end = intervals[i]
            if next_end < cur_end:  # 覆盖
                continue
            elif next_start <= cur_end:  # 可合并
                res.pop()
                res.append([cur_start, next_end])
                next_start = cur_start
            elif next_start > cur_end:
                res.append([next_start, next_end])
            cur_start, cur_end = next_start, next_end
        return res

    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # A B 两列表都是不相交的区间
        # 从最小的区间开始，计算完相交就pop掉 每个区间至多只能相交一次
        # 双指针
        if not firstList or not secondList:
            return []
        res = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            low = max(firstList[i][0], secondList[j][0])
            high = min(firstList[i][1], secondList[j][1])
            if low <= high:
                res.append([low, high])
            if firstList[i][1] > secondList[j][1]:  # 谁小谁往后走
                j += 1
            else:
                i += 1
        return res


solve = Solution()
# intervals = [[1, 2], [1, 2], [1, 2]]
# print(solve.eraseOverlapIntervals(intervals))
# points = [[1, 2], [2, 3], [3, 4], [4, 5]]
# print(solve.findMinArrowShots(intervals))
# print(solve.findMinArrowShots(points))
# clips = [[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [1, 3], [4, 7],
#          [1, 4], [2, 5], [2, 6], [3, 4], [4, 5], [5, 7], [6, 9]]
# print(solve.videoStitching(clips, 9))
# intervals = [[1, 4], [3, 6], [2, 8]]
# print(solve.removeCoveredIntervals(intervals))
# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# print(solve.merge(intervals))
first = [[3, 5], [9, 20]]
second = [[4, 5], [7, 10], [11, 12], [14, 15], [16, 20]]
print(solve.intervalIntersection(first, second))
