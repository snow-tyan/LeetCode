'''
股票问题
121.买卖股票最佳时机
122.买卖股票最佳时机II
123.买卖股票最佳时机III
188.买卖股票最佳时机IV
309.最佳买卖股票时机含冷冻期  难
714.买卖股票最佳时机含手续费
'''
from typing import List


class Solution:
    # 只能买卖一次 暴力+贪心+DP
    def maxProfit(self, prices: List[int]) -> int:
        # # 股票只能买卖一次
        # # 暴力，找最大间距
        # n = len(prices)
        # res = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         res = max(res, prices[j] - prices[i])
        # return res

        # # 贪心 找最小左值和最大右值
        # n = len(prices)
        # res = 0
        # left = float('inf')
        # for i in range(n):
        #     left = min(left, prices[i])
        #     res = max(res, prices[i] - left)
        # return res

        # dp 想获得最大利润
        # 用两列的数组 dp[i][0] dp[i][1]
        # 分别表示第i天持有股票所得最多现金和不持有股票所得最多现金
        # 递推：第i天持有 = 第i-1天持有 或 第i天买入 二者取最大
        #      第i天不持有 = 第i-1天不持有 或 第i天卖出 取最大
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        # base case
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], -prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])  # 第i天卖出说明第i-1天持有
        return dp[n - 1][1]

    # 可以多次买卖 贪心+DP
    def maxProfitII(self, prices: List[int]) -> int:
        # # 贪心就是底点买入，高点卖出
        # # 求差分数组，正的就表示买卖
        # res = 0
        # n = len(prices)
        # for i in range(1, n):
        #     res += max((prices[i]-prices[i - 1]), 0)
        # return res

        # 两种状态 持有/不持有
        # dp[i][0] 第i天持有所得最大金额 = max(第i-1天持有, 第i天买入)
        # dp[i][1] 第i天不持有所得最大金额 = max(第i-1天不持有, 第i天卖出)
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])  # 第i天买入=第i-1天不持有-当天买入价
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])  # 第i天卖出=第i-1天持有+当天卖出价
        return dp[n - 1][1]

    # 至多买卖两次
    def maxProfitIII(self, prices: List[int]) -> int:
        # 五种状态：
        # 0 无操作
        # 1 第一次买入 第i天持有 = max(第i-1天持有， 第i天买入)
        # 2 第一次卖出 第i天不持有 = max(第i-1天不持有， 第i天卖出)
        # 3 第二次买入 第i天持有 = max(第i-1天持有， 第i天买入)
        # 4 第二次卖出 第i天不持有 = max(第i-1天不持有， 第i天卖出)
        n = len(prices)
        dp = [[0] * 5 for _ in range(n)]
        # base case
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        dp[0][3] = -prices[0]
        dp[0][4] = 0
        for i in range(1, n):
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])  # 当天买入
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])  # 当天卖出
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])  # 第二次买入
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])  # 第二次卖出
        return dp[n - 1][4]

    # 至多K次买卖
    def maxProfitIV(self, k: int, prices: List[int]) -> int:
        # From maxProfitIII
        # 0 1 2 3 4 ......  2*k次操作
        n = len(prices)
        dp = [[0] * (2 * k + 1) for _ in range(n)]
        # base case
        for j in range(k):
            dp[0][2 * j + 1] = -prices[0]
        for i in range(1, n):
            for j in range(1, 2 * k + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + (-1) ** j * prices[i])
        return dp[n - 1][2 * k]

    # 卖出后有一天冷冻期
    def maxProfitFreeze(self, prices: List[int]) -> int:
        # 四种状态 （卖出和不持有分开）
        # 0 今天持有 = 之前持有 或 今天刚买(昨天是冷冻期，昨天不是冷冻期)
        # 1 今天不持有 = 之前就不持有 或 今天是冷冻期
        # 2 今天卖出 = 昨天持有
        # 3 今天是冷冻期 = 前一天卖的
        n = len(prices)
        dp = [[0] * 4 for _ in range(n)]
        # base case
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        dp[0][2] = 0
        dp[0][3] = 0
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], max(dp[i - 1][1], dp[i - 1][3]) - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][3])
            dp[i][2] = dp[i - 1][0] + prices[i]
            dp[i][3] = dp[i - 1][2]
        return max(dp[n - 1][1:])

    # 含手续费 完全=maxProfitII
    def maxProfitFee(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])  # 第i天买入=第i-1天不持有-当天买入价
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i] - fee)  # 第i天卖出=第i-1天持有+当天卖出价
        return dp[n - 1][1]


solve = Solution()
# prices = []
# print(solve.maxProfitIII(prices))
# print(solve.maxProfitIV(prices=prices, k=2))
