'''
滑窗
485.最大连续1的个数
487.最大连续1的个数II
1004.最大连续1的个数III
'''
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # 数1
        res = 0
        cnt = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                cnt += 1
            else:  # 碰到0就更新res
                res = max(res, cnt)  # 记录
                cnt = 0
        res = max(res, cnt)
        return res

    def findMaxConsecutiveOnesII(self, nums: List[int]) -> int:
        # 滑窗
        n = len(nums)
        left, right, cnt = 0, 0, 0  # cnt记录出现0的个数
        res = 0
        while right < n:
            # 控制窗口右端点
            while right < n and cnt <= 1:  # 窗口内0的个数<=1，右窗口就一直前移
                if nums[right] == 0:
                    cnt += 1
                right += 1
                if cnt <= 1:  # 更新窗口大小
                    res = max(res, right - left)
            # 控制窗口左端点
            while left <= right and cnt > 1:  # 窗口内0的个数>1，左端口就一直前移
                if nums[left] == 0:
                    cnt -= 1
                left += 1
        return res

    def longestOnes(self, nums: List[int], k: int) -> int:
        # 滑窗，和II及其相似
        n = len(nums)
        left, right, cnt = 0, 0, 0
        res = 0
        while right < n:
            while right < n and cnt <= k:  # 控制窗口内0的次数<=k
                if nums[right] == 0:
                    cnt += 1
                right += 1
                if cnt <= k:
                    res = max(res, right - left)
            while left <= right and cnt > k:
                if nums[left] == 0:
                    cnt -= 1
                left += 1
        return res