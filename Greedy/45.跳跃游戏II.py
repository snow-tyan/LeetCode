'''
贪心算法：每次找局部最优解->全局最优解
45.跳跃游戏II
55.跳跃游戏
'''
from typing import List


class Solution:
    # dp O(N*nums[i])
    def jumpDP(self, nums: List[int]) -> int:
        # dp[i] 记录跳到第i个位置最小次数
        # dp[i+j]=min(dp[i+j], dp[i]+1)  0<=j<=nums[i]
        n = len(nums)
        dp = [float('inf')] * n
        # base case
        dp[0] = 0
        for i in range(n):
            for j in range(1, nums[i] + 1):
                if i + j < n:  # 下标合法
                    dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[n - 1]

    # greedy O(N)
    def jump(self, nums: List[int]) -> int:
        boundry = 0
        step = 0
        max_pos = 0
        for i in range(len(nums) - 1):
            max_pos = max(max_pos, i + nums[i])
            if i == boundry:
                boundry = max_pos
                step += 1
        return step

    def canJump(self, nums: List[int]) -> bool:
        # 思路1 找0，碰到零判断能不能越过，若不能直接返回False
        # 思路2 贪心 维护一个最大可到达距离dis
        # 若i可到达，则i+nums[i]内所有位置必可到达。dis超过n时返回真
        if 0 not in nums:
            return True
        n, dis = len(nums), 0
        for i in range(n):
            if i <= dis:
                dis = max(dis, i + nums[i])
                if dis >= n - 1:
                    return True
        return False


solve = Solution()
nums = [2, 5]
# print(solve.jumpDP(nums))
# print(solve.jump(nums))
print(solve.canJump(nums))
