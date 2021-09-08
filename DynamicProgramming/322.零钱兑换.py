'''
322.零钱兑换

完全背包
518.零钱兑换II  组合问题 -- 70.爬楼梯  (vs 零钱兑换II)  排列问题

'''
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] amount=i时 所需最小硬币数
        # dp[i] = min(dp[i], dp[i-coin]+1)
        dp = [amount + 1] * (amount + 1)  # 初始化为amount+1，因为不可能大于这个数
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:  # 不合法，跳过
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] == amount + 1:  # 大于amount，说明找不到组合
            return -1
        return dp[amount]

    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i][j] 表示 前i种硬币 恰好组成金额j的组合数
        # 第i种硬币选0个，1个，...，k个
        # dp[i][j] = dp[i-1][j]+dp[i-1][j-coins[i]]+...+dp[i-1][j-k*coins[i]]
        #          = dp[i-1][j]+dp[i][j-coins[i]]
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        # base case
        # dp[0][j]=0, dp[i][0]=1
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if j - coins[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]

        return dp[n][amount]

        # dp = [0] * (amount + 1)
        # dp[0] = 1
        # for coin in coins:
        #     for i in range(coin, amount + 1):
        #         if coin <= i:
        #             dp[i] += dp[i - coin]
        #
        # return dp[amount]


amount = 5
coins = [1, 2, 5]
solve = Solution()
print(solve.change(amount, coins))
