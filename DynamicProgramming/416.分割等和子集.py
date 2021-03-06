'''
01 背包
416.分割等和子集
494.目标和
1049.最后一块儿石头重量II
474.一和零
879.盈利计划 hard
'''
from typing import List, Tuple
import numpy as np


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # target=sum(nums)/2 -> sum(nums)必是偶数
        # 求nums子集和是否可以是target
        # 01背包问题 dp[i][j]表示[0,i]区间内选取若干个正整数，其和是否可以为j
        # dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i]]
        # if sum(nums) % 2 != 0:
        #     return False
        # target = sum(nums) // 2
        # n = len(nums)
        # dp = [[False] * (target + 1) for _ in range(n)]
        # # base case
        # # dp[0][0]=False; dp[i][0]=True 选取0个正整数，其和为0
        # for i in range(1, n):
        #     dp[i][0] = True
        # dp[0][nums[0]] = True  # [0,0]区间内，选1个正整数，其和为nums[0]
        # for i in range(n):
        #     for j in range(1, target + 1):
        #         if j - nums[i] < 0:
        #             dp[i][j] = dp[i - 1][j]
        #         else:
        #             dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]

        # return dp[n - 1][target]

        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        n = len(nums)
        dp = [False] * (target + 1)
        # base case
        dp[0] = True
        for i in range(n):
            for j in range(target, nums[i] - 1, -1):
                dp[j] |= dp[j - nums[i]]

        return dp[target]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 向nums每个数字前添+-号使和为target
        # nums分成两部分，A全添加加号，B全添减号
        # sum(A)-sum(B)=target
        # 又sum(A)+sum(B)=sum(nums)
        # 得sum(A)=(target+sum(nums))/2
        # 问题转化成了在nums中找使得和为(target+sum(nums))/2的方案数
        # dp[i][j] 表示前i个数和为j的方案数
        # dp[i][j]=dp[i-1][j]+dp[i-1][j-nums[i]]

        # n = len(nums)
        # A = sum(nums) + target  # 2*sum(A)
        # new_target = A // 2
        # if A < 0 or A % 2 != 0:  # A全添加号，必非负；又=2*sum(A)，必为偶数
        #     return 0
        # dp = [[0] * (new_target + 1) for _ in range(n + 1)]
        # # 边界
        # dp[0][0] = 1
        #
        # for i in range(1, n + 1):
        #     for j in range(new_target + 1):
        #         dp[i][j] = dp[i - 1][j]
        #         if j >= nums[i - 1]:
        #             dp[i][j] += dp[i - 1][j - nums[i - 1]]
        #
        # return dp[n][new_target]

        n = len(nums)
        n_target = sum(nums) + target  # sum(A) 天然不小于0
        if n_target < 0 or n_target % 2 != 0:
            return 0
        n_target //= 2  # 背包容量
        dp = [0] * (n_target + 1)  # 填满容量i的背包，有dp[i]种方案
        # base case
        dp[0] = 1
        for i in range(n):
            for j in range(n_target, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]  # 填满背包有多少种方案，常用递推公式
        return dp[n_target]

    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 像极了目标和
        # 给stone数组添加+-号，使其和最小
        # sigma=sum(stones)-2*target, 要使sigma最小，求target最大就行了
        # 显然target有最大值sum(stones)//2
        # dp[i][j] 前i个石头凑和不超过j的最大价值
        target = sum(stones) // 2
        dp = [0] * (target + 1)
        dp[0] = 0
        for stone in stones:
            for j in range(target, stone - 1, -1):
                dp[j] = max(dp[j], dp[j - stone] + stone)

        return sum(stones) - 2 * dp[target]

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 01背包，每个字符串只能放一次 一个背包 两个维度
        # dp[i][j][k] 前i个字符串包含j个0和k个1的最大子集的size
        # dp[i][j][k]=max(dp[i-1][j][k],
        #                 dp[i-1][j-str0][k-str1]+1)

        # 返回0和1的数目
        def count_zero_one(s: str) -> Tuple[int, int]:
            zero, one = 0, 0
            for ch in s:
                if ch == '0':
                    zero += 1
                else:
                    one += 1
            return zero, one

        dp = [[0] * (n + 1) for _ in range(m + 1)]  # int[m+1][n+1]
        # base case dp[0][j]=dp[i][0]=0
        for s in strs:
            zero, one = count_zero_one(s)
            for j in range(m, zero - 1, -1):  # [zero, m]
                for k in range(n, one - 1, -1):  # [one, n]
                    dp[j][k] = max(dp[j][k], dp[j - zero][k - one] + 1)
        return dp[m][n]

    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        # 返回结果模1e9+7
        # 01背包，每名员工只能参加一项工作
        # 背包容量n, 物品重量group[i], 物品价值profit[i], 要求至少产生minProfit利润
        # dp[i][j][k] 前i个物品容量j产生至少价值k的方案数
        # MOD = 10 ** 9 + 7
        # m = len(group)
        # int[m+1][n+1][minProfit+1]
        # dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(m + 1)]
        # # base case
        # dp[0][0][0] = 1
        # for i in range(1, m + 1):  # group[i-1]
        #     for j in range(n + 1):
        #         for k in range(minProfit + 1):
        #             if j - group[i - 1] < 0:
        #                 dp[i][j][k] = dp[i - 1][j][k]
        #             else:
        #                 dp[i][j][k] = (dp[i - 1][j][k] + dp[i - 1][j - group[i - 1]][max(0, k - profit[i - 1])]) % MOD
        #
        # total = sum(dp[m][j][minProfit] for j in range(n + 1))
        # return total % MOD

        MOD = 10 ** 9 + 7
        m = len(group)
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, m + 1):
            for j in range(n, group[i - 1] - 1, -1):
                for k in range(minProfit, -1, -1):
                    dp[j][k] = (dp[j][k] + dp[j - group[i - 1]][max(0, k - profit[i - 1])]) % MOD
        total = sum(dp[j][minProfit] for j in range(n + 1))
        return total % MOD


solve = Solution()
# nums = [1, 5, 3, 5]
# strs = ["10", "0001", "111001", "1", "0"]
# m = 5
# n = 3

n = 10
minProfit = 5
group = [2, 3, 5]
profit = [6, 7, 8]
print(solve.profitableSchemes(n, minProfit, group, profit))
