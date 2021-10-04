'''
9.15 每日一题
162.寻找峰值
'''
from typing import List
import random


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 方法一：最大值一定是峰值 O(N)
        # 方法二：爬坡
        # 随机选一点，若nums[i]<nums[i+1]往右走，否则往左走 O(N)
        # 类似二分法，不断选中点爬坡 O(logN)
        n = len(nums)
        nums.append(float('-inf'))  # 假设nums[-1]=nums[n]=负无穷
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1
        return -1


solve = Solution()
nums = [1, 2, 1, 3, 5, 6, 4]
print(solve.findPeakElement(nums))
