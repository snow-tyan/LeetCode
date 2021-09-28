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
    # # dp[i][j] 下标0-i的物品，背包容量为j时，所装最大价值
    # dp = [[0] * (W + 1) for _ in range(N)]  # N=len(wt)=len(val)
    # # base case
    # # dp[i][0] = 0
    # for j in range(wt[0]):  # j<wt[0]
    #     dp[0][j] = 0
    # for j in range(wt[0], W + 1):  # j>=wt[0]
    #     dp[0][j] = val[0]
    # for i in range(1, N):  # 遍历物品i
    #     for j in range(W + 1):  # 遍历背包容量j
    #         if j < wt[i]:
    #             dp[i][j] = dp[i - 1][j]
    #         else:
    #             dp[i][j] = max(dp[i - 1][j],  # 不把第i个物品装进背包
    #                            dp[i - 1][j - wt[i]] + val[i])  # 把第i个物品装进背包
    # return dp[N - 1][W]

    # 空间优化
    dp = [0] * (W + 1)
    # base case
    # dp[0] = 0
    for i in range(N):
        for j in range(W, wt[i] - 1, -1):  # 从后往前遍历[W，wt[i]]
            # 倒序为了保证物品i只被放入一次 每次取得的状态不会和上一次重合
            # 也是因为倒序，所以遍历顺序不能改 先物品再背包容量
            dp[j] = max(dp[j],  # 不把第i个物品装进背包
                        # i从0开始无需偏移
                        dp[j - wt[i]] + val[i])  # 把第i个物品装进背包
    return dp[W]


# 完全背包
def complete_knapsack(W: int, N: int, wt: List[int], val: List[int]) -> int:
    # # dp[i][j] 下标0-i的物品，背包容量为j时，所装最大价值
    # dp = [[0] * (W + 1) for _ in range(N)]
    # base case
    # # dp[i][0] = 0
    # for j in range(wt[0]):  # j<wt[0]
    #     dp[0][j] = 0
    # for j in range(wt[0], W + 1):  # j>=wt[0]
    #     dp[0][j] = val[0]
    # for i in range(1, N):  # 遍历物品i
    #     for j in range(W + 1):  # 遍历背包容量j
    #         if j < wt[i]:
    #             dp[i][j] = dp[i - 1][j]
    #         else:
    #             dp[i][j] = max(dp[i - 1][j],  # 不把第i个物品装进背包
    #                            dp[i][j - wt[i]] + val[i])  # 把第i个物品装进背包
    # return dp[N - 1][W]

    # 空间优化
    dp = [0] * (W + 1)
    # base case
    # dp[0] = 0
    for i in range(N):
        for j in range(wt[i], W + 1):  # [wt[i], W]
            # 遍历顺序可以改，先物品先背包容量
            dp[j] = max(dp[j], dp[j - wt[i]] + val[i])
    return dp[W]


N = 3
W = 4
wt = [2, 1, 3]
val = [4, 2, 3]
print(knapsack(W, N, wt, val))
print(complete_knapsack(W, N, wt, val))
