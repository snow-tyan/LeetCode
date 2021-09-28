'''
62.不同路径
63.不同路径II
343.整数拆分 剑指offer14-I.剪绳子
96.不同的二叉搜索树
'''
from typing import List
import copy


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j]从start出发到i,j共有不同路径
        # dp[i][j]=dp[i-1][j]+dp[i][j-1]
        dp = [[0] * n for _ in range(m)]
        # base case
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        # base case
        for i in range(m):
            dp[i][0] = 1
            if obstacleGrid[i][0] == 1:
                # for k in range(i, m):
                #     dp[k][0] = 0
                break
        for j in range(n):
            dp[0][j] = 1
            if obstacleGrid[0][j] == 1:
                # for k in range(j, n):
                #     dp[0][k] = 0
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    def integerBreak(self, n: int) -> int:
        # dp[i] 分拆数字i，所得最大乘积
        # 分拆成多少个，不知道，要么两个 要么 多个(怎么表示)
        # 假设整数i拆出来第一个整数为j(j固定,遍历j),剩下i-j(拆或不拆)
        # dp[i]=max(j*dp[i-j],j*(i-j))
        # 1<=j<i需要遍历所有的j使得dp[i]最大,因此dp[i]=max(dp[i],j*dp[i-j],j*(i-j))
        dp = [0] * (n + 1)
        # base case
        # dp[2] = 1
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * dp[i - j], j * (i - j))
        print(dp)
        return dp[n]

    def numTrees(self, n: int) -> int:
        # dp[i] 由i个节点组成的BST个数
        # 以j为头结点，左子树BST个数 dp[j-1]
        # 以j为头结点，右子树BST个数 dp[i-j]
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            for j in range(1, i + 1):  # 遍历j充当头结点 1<=j<=i
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]
