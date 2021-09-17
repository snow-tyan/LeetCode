'''
子集问题
78.子集
90.子集II
491.递增子序列
'''
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 方法一：回溯
        # def backtracking(start_idx: int) -> None:
        #     res.append(path[:])
        #     for i in range(start_idx, len(nums)):
        #         path.append(nums[i])
        #         backtracking(i + 1)
        #         path.pop()
        #
        # res = []
        # path = []
        # backtracking(0)
        # return res

        # 方法二：遍历，后面每个数加上前面的数
        res = [[]]
        for num in nums:
            for r in res[:]:
                res.append(r + [num])

        return res


solve = Solution()
print(solve.subsets([1, 2, 3]))
