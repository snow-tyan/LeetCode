'''
双指针
27.移除元素
26.删除排序数组中的重复项
283.移动零
844.比较含退格的字符串
977.有序数组的平方
'''
from typing import List


class Solution:
    # 原地移除val，并返回len(nums)
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] == val:
                continue
            nums[slow] = nums[fast]  # inplace
            slow += 1
        return slow


solve = Solution()
print(solve.removeElement([3, 2, 2, 3], 3))
