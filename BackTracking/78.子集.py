'''
子集问题
78.子集
90.子集II
491.递增子序列
'''
from typing import List


class Solution:
    # nums 不重复，返回其所有子集
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 方法一：回溯
        def backtracking(start_idx: int) -> None:
            res.append(path[:])  # 收集子集
            # 递归终止 start==len(nums)时循环也就结束了
            # if start_idx == len(nums):
            #     return
            for i in range(start_idx, len(nums)):
                path.append(nums[i])
                backtracking(i + 1)
                path.pop()

        res = []
        path = []
        backtracking(0)
        return res

        # # 方法二：遍历，后面每个数加上前面的数
        # res = [[]]
        # for num in nums:
        #     for r in res[:]:
        #         res.append(r + [num])
        #
        # return res

    # nums 有重复，返回其所有子集，子集不可重复
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        def backtracking(start_idx: int) -> None:
            res.append(path[:])  # 收集子集
            for i in range(start_idx, len(nums)):
                if i > start_idx and nums[i] == nums[i - 1]:  # 树层去重大法好
                    continue
                path.append(nums[i])
                backtracking(i + 1)
                path.pop()

        res = []
        path = []
        nums.sort()
        backtracking(0)
        return res

    # 返回所有递增子序列
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtracking(start_idx: int) -> None:
            if len(path) > 1:
                res.append(path[:])
            # used放在回溯函数内部
            # 保证控制的是同一树层的元素不能重复选取
            used = [0] * 201  # -100<=nums[i]<=100
            for i in range(start_idx, len(nums)):
                if used[nums[i] + 100] or path and nums[i] < path[-1]:
                    continue
                used[nums[i] + 100] = 1
                path.append(nums[i])
                backtracking(i + 1)
                path.pop()

        res = []
        path = []
        backtracking(0)
        return res


solve = Solution()
# print(solve.subsets([1, 2, 3]))
# print(solve.subsets2([1, 2, 2]))
print(solve.findSubsequences([4, 7, 6, 7]))
