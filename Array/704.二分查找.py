'''
二分查找
704.二分查找
35.搜索插入位置
34.在排序数组中查找元素的第一个和最后一个位置  细节
69.x的平方根
367.有效的完全平方数
'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 双指针
        left, right = 0, len(nums) - 1
        while left <= right:
            # mid = (left + right) // 2  # 先算和有溢出的风险
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 查询target最左边位置，如没有返回应插入位置
        def binarySearch(target: int) -> int:
            left, right = 0, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        result = []
        n = len(nums)
        left_idx = binarySearch(target)
        right_idx = binarySearch(target + 1) - 1
        result.extend([left_idx, right_idx])
        if left_idx == n or nums[left_idx] != target:
            return [-1, -1]
        return result

    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return right

    def isPerfectSquare(self, num: int) -> bool:
        # 返回sqrt整数部分
        def Sqrt(x: int) -> int:
            left, right = 0, x
            while left <= right:
                mid = left + (right - left) // 2
                if mid * mid > x:
                    right = mid - 1
                else:
                    left = mid + 1
            return right

        sqrt_num = Sqrt(num)
        if sqrt_num * sqrt_num == num:
            return True
        return False


solve = Solution()
# print(solve.searchInsert([1, 3, 4, 6], 5))
print(solve.searchRange([], 10))
