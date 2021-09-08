'''
0-1 背包
容量为W的背包，N个物品，每个物品都有重量wt[i]和价值val[i]，最多能装的价值？
每个物品只能选一次

完全背包
每个物品可以选多次
'''
from typing import List


# 0-1背包
def knapsack(W: int, N: int, wt: List[int], val: List[int]) -> int:
    # dp[i][j] 前i个物品，背包容量为j时，所装最大价值
    # dp = [[0] * (W + 1) for _ in range(N + 1)]
    # # base case: dp[0][j]=dp[i][0]=0
    # for i in range(1, N + 1):
    #     for j in range(1, W + 1):
    #         if j < wt[i - 1]:
    #             dp[i][j] = dp[i - 1][j]
    #         else:
    #             dp[i][j] = max(dp[i - 1][j],  # 不把第i个物品装进背包
    #                            # i从1开始，wt[i-1]和val[i-1]是索引偏移
    #                            dp[i - 1][j - wt[i - 1]] + val[i - 1])  # 把第i个物品装进背包
    # return dp[N][W]

    # 空间优化
    dp = [0] * (W + 1)
    # base case
    # dp[0] = 0
    for i in range(N):
        for j in range(W, wt[i] - 1, -1):  # 从后往前遍历[W，wt[i]]
            # 从后往前遍历，保证递推是由上一个物品时留下的数组更新过来的
            # 不用判断j-wt[i]>=0是因为循环到j==wt[i]就停了
            dp[j] = max(dp[j],  # 不把第i个物品装进背包
                        # i从0开始无需偏移
                        dp[j - wt[i]] + val[i])  # 把第i个物品装进背包
    return dp[W]


# 完全背包
def complete_knapsack(W: int, N: int, wt: List[int], val: List[int]) -> int:
    # # dp[i][j] 前i个物品，背包容量为j时，所装最大价值
    # dp = [[0] * (W + 1) for _ in range(N + 1)]
    # # base case: dp[0][j]=dp[i][0]=0
    # for i in range(1, N + 1):
    #     for j in range(1, W + 1):
    #         if j < wt[i - 1]:
    #             dp[i][j] = dp[i - 1][j]
    #         else:
    #             dp[i][j] = max(dp[i - 1][j],  # 不把第i个物品装进背包
    #                            # i从1开始，wt[i-1]和val[i-1]是索引偏移
    #                            dp[j][j - wt[i - 1]] + val[i - 1])  # 把第i个物品装进背包
    # return dp[N][W]

    # 空间优化
    dp = [0] * (W + 1)
    # base case
    # dp[0] = 0
    for i in range(N):
        for j in range(wt[i], W + 1):  # [wt[i], W]
            dp[j] = max(dp[j], dp[j - wt[i]] + val[i])
    return dp[W]


N = 3
W = 4
wt = [2, 1, 3]
val = [4, 2, 3]
print(knapsack(W, N, wt, val))
print(complete_knapsack(W, N, wt, val))
