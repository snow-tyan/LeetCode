'''
完全背包
322.零钱兑换
518.零钱兑换II  组合问题 -- 70.爬楼梯  (vs 零钱兑换II)  排列问题
    # 爬楼梯若改成数组传参，一次可以爬几层，问有几种方法爬到楼顶，就是个完全背包排列问题
377.组合总和IV  排列问题
139.单词拆分 dfs+bfs+dp
279.完全平方数 bfs+dp+贪心
1449.数位成本和为目标值的最大数字 hard
'''
from typing import List
import math


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # # dp[i] amount=i时 所需最小硬币数
        # # dp[i] = min(dp[i], dp[i-coin]+1)
        # dp = [amount + 1] * (amount + 1)  # 初始化为amount+1，因为不可能大于这个数
        # dp[0] = 0
        # for i in range(1, amount + 1):
        #     for coin in coins:
        #         if i - coin < 0:  # 不合法，跳过
        #             continue
        #         dp[i] = min(dp[i], dp[i - coin] + 1)
        # if dp[amount] == amount + 1:  # 大于amount，说明找不到组合
        #     return -1
        # return dp[amount]

        n = len(coins)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(n):
            for j in range(coins[i], amount + 1):
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

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

    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 完全背包，nums[i]可以多次取用
        # dp[i][j] 组合长度为i，和为j的组合个数，那么 0<=i,j<=target 和完全背包略有区别
        # 若要用二维dp做，最后要对dp[i][target]求最后一列之和，二维还挺复杂，mark
        # 而一维只要调换内外循环就可以规避掉

        dp = [0] * (target + 1)
        dp[0] = 1
        for j in range(1, target + 1):
            for num in nums:  # 之所以要放到内循环，保证每次都从头开始取
                if j >= num:
                    dp[j] += dp[j - num]
        return dp[target]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] s[:i]能否break
        # 取决于：
        # 1 其前缀子串s[:j]是否为True -> dp[j] (j遍历指针,0<=j<=i)
        # 2 剩余子串s[j:i]是否在单词表中
        n = len(s)
        dp = [False] * (n + 1)
        # base case
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i - 1, -1, -1):
                if dp[i]:
                    break
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[n]

    def numSquares(self, n: int) -> int:
        # 转换为完全背包
        # 给定1,4,9,16,... 求组成n的最小数量，每个数字无限次
        square = [i * i for i in range(1, 1 + int(math.sqrt(n)))]
        print(square)
        m = len(square)
        dp = [float('inf')] * (n + 1)
        # base case
        dp[0] = 0
        for i in range(m):
            for j in range(square[i], n + 1):
                dp[j] = min(dp[j], dp[j - square[i]] + 1)
        return dp[n]

    def largestNumber(self, cost: List[int], target: int) -> str:
        # cost为数位成本，length==9 添加的数位中只有1-9
        # 数位i+1的成本为cost[i] 0<=i<=8
        # 完全背包 恰好装满背包容量target，物品重量cost[i]，物品价值1
        # 1 位数越多越好 2 数字从大小排  -> dp解决1，贪心解决2
        # dp[i+1][j] 使用前i个数位总成本为j时的最大位数
        # base case dp[0][j]=dp[i][0]=负无穷 dp[0][0]=0
        # dp[9][target]即为可以得到的最大位数 若<0则直接返回0
        # 用where[i+1][j]记录
        # dp = [[float('-inf')] * (target + 1) for _ in range(10)]
        # dp[0][0] = 0
        #
        # for i in range(len(cost)):
        #     for j in range(target + 1):
        #         if j < cost[i]:
        #             dp[i + 1][j] = dp[i][j]
        #         else:
        #             dp[i + 1][j] = max(dp[i][j], dp[i + 1][j - cost[i]] + 1)
        #
        # if dp[9][target] < 0:
        #     return '0'
        #
        # res = ''
        # # 当得到位数后，用贪心从9往1搜索
        # j = target
        # for i in range(8, -1, -1):
        #     while cost[i] <= j and dp[i + 1][j] == dp[i + 1][j - cost[i]] + 1:
        #         res += str(i + 1)
        #         j -= cost[i]
        #
        # return res

        dp = [float('-inf')] * (target + 1)
        dp[0] = 0

        for i in range(len(cost)):
            for j in range(cost[i], target + 1):
                dp[j] = max(dp[j], dp[j - cost[i]] + 1)

        if dp[target] < 0:
            return '0'

        res = ''
        # 当得到位数后，用贪心从9往1搜索
        j = target
        for i in range(8, -1, -1):
            # 如果状态能够由数值转移而来，则选择该值
            while cost[i] <= j and dp[j] == dp[j - cost[i]] + 1:
                res += str(i + 1)
                j -= cost[i]

        return res


amount = 5
coins = [1, 2, 5]
solve = Solution()
# print(solve.change(amount, coins))
# n = 12
# print(solve.numSquares(n))

cost = [4, 3, 2, 5, 6, 7, 2, 5, 5]
target = 9
print(solve.largestNumber(cost, target))
