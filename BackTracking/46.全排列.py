'''
排列问题
46.全排列
47.全排列II
'''
from typing import List


class Solution:
    # nums不重复，求全排列
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking() -> None:
            if len(path) == n:
                res.append(path[:])
                return
            for i in range(n):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtracking()
                path.pop()
                used[i] = False

        res = []
        n = len(nums)
        path = []
        used = [False] * n
        backtracking()
        return res

    # nums有重复元素，求不重复的全排列
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtracking() -> None:
            if len(path) == n:
                res.append(path[:])
                return
            for i in range(n):
                # used[i-1]=False意味着同一树层上 前一个已经取用过了
                # used[i-1]=True意味着同一树枝上 前一个已经取用过了
                if used[i] or i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtracking()
                path.pop()
                used[i] = False

        res = []
        n = len(nums)
        path = []
        used = [False] * n
        nums.sort()
        backtracking()
        return res


solve = Solution()
# print(solve.permute([1, 2, 3]))
print(solve.permuteUnique([1, 1, 2]))
