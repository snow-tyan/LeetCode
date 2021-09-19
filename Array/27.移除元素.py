'''
双指针
27.移除元素
26.删除排序数组中的重复项
283.移动零
844.比较含退格的字符串 简单题？
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
        print(nums)
        return slow

    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] == nums[slow]:
                continue
            nums[slow + 1] = nums[fast]
            slow += 1
        print(nums)
        return slow + 1

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # 快慢指针 原地删除0, 然后在慢指针后补0
        # slow = 0
        # n = len(nums)
        # for fast in range(n):
        #     if nums[fast] == 0:
        #         continue
        #     nums[slow] = nums[fast]
        #     slow += 1
        # while slow < n:
        #     nums[slow] = 0
        #     slow += 1

        # 方法二：遇到就交换 快指针遍历一遍
        slow = 0
        n = len(nums)
        for fast in range(n):
            # 当前元素!=0，就把其交换到左边，等于0的交换到右边
            if nums[fast] == 0:
                continue
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

    def backspaceCompare(self, s: str, t: str) -> bool:
        # 方法一：如果可以用额外空间，用栈模拟结果
        # 方法二：双指针 细节有点多
        i, j = len(s) - 1, len(t) - 1
        counti = countj = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == "#":
                    counti += 1
                    i -= 1
                elif counti > 0:
                    counti -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if t[j] == "#":
                    countj += 1
                    j -= 1
                elif countj > 0:
                    countj -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1

        return True

    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 平方后像一个y=x^2抛物线
        # 双指针 从两边向中间比较
        n = len(nums)
        res = [0] * n
        i, j = 0, n - 1
        pos = n - 1
        while pos >= 0:
            if nums[i] * nums[i] < nums[j] * nums[j]:
                res[pos] = nums[j] * nums[j]
                j -= 1
            else:
                res[pos] = nums[i] * nums[i]
                i += 1
            pos -= 1
        return res


solve = Solution()
# print(solve.removeElement([0, 1, 0, 3, 12], 0))
# print(solve.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(solve.backspaceCompare(s='xywrrmp', t="xywrrmu#p"))
