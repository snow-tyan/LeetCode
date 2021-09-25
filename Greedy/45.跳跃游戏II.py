'''
贪心算法：每次找局部最优解->全局最优解
45.跳跃游戏II
55.跳跃游戏
1005.k次取反后最大化的数组和
763.划分字母区间
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
        boundry = 0  # 当前最大可到达
        step = 0
        max_pos = 0  # 下一步最大可到达距离
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

    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # 按绝对值大小排序
        # 贪心策略：尽可能把大的负数翻正，无可奈何情况下把最小的整数翻负
        n = len(nums)
        nums.sort(key=lambda x: abs(x))
        # print(nums)
        # 倒序找大负数翻正
        i = n - 1
        while i >= 0 and k > 0:
            if nums[i] < 0:
                nums[i] *= -1
                k -= 1
            if nums[i] == 0:  # 如果有0喜闻乐见 直接消耗剩下的k次
                k = 0
            i -= 1
        # 如果此时k还大于0 只对最小的正数操作 k为偶数无操作
        if k > 0 and k % 2 != 0:
            nums[0] = nums[0] * -1
        return sum(nums)

    def partitionLabels(self, s: str) -> List[int]:
        # 找每个字母最远出现下标
        alpha = [0] * 26
        for i, ch in enumerate(s):
            alpha[ord(ch) - ord('a')] = i

        res = []
        left, right = 0, 0
        for i, ch in enumerate(s):
            right = max(right, alpha[ord(ch) - ord('a')])
            if i == right:  # 找到分割点
                res.append(right - left + 1)
                left = right + 1
        return res


solve = Solution()
nums = [2, 5]
# print(solve.jumpDP(nums))
# print(solve.jump(nums))
print(solve.canJump(nums))
