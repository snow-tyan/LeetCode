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


nums = []
target = -1
solve = Solution()
print(solve.search(nums, target))
