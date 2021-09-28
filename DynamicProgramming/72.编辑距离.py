'''
72.编辑距离
583.两个字符串的删除操作 低配编辑距离
931.下降路径最小和
'''
from typing import List
import copy


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 返回将word1编辑成word2的最小操作数(增，删，改)
        # dp[i][j] word1前i个字符变到word2前j个字符的最小编辑距离
        # 则 增dp[i][j-1] 删dp[i-1][j] 改dp[i-1][j-1]
        n = len(word1)
        m = len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # 边界
        for i in range(1, n + 1):
            dp[i][0] = i
        for j in range(1, m + 1):
            dp[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j],
                                       dp[i][j - 1],
                                       dp[i - 1][j - 1])

        return dp[n][m]

    # 低配版编辑距离
    def minDistanceSimple(self, word1: str, word2: str) -> int:
        # 找word1 word2相同的部分
        # 即找word1编辑到word2的最小编辑距离 删+增
        # dp[i][j] word1前i个字符变到word2前j个字符的最小编辑距离
        # 则 增dp[i][j-1] 删dp[i-1][j] 改dp[i-1][j-1]
        n = len(word1)
        m = len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # 边界
        for i in range(1, n + 1):
            dp[i][0] = i
        for j in range(1, m + 1):
            dp[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
        return dp[n][m]

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # n = len(matrix)
        # dp = matrix.copy()
        # for i in range(1, n):
        #     for j in range(n):
        #         if j == 0:
        #             dp[i][j] = min(matrix[i - 1][j], matrix[i - 1][j + 1]) + matrix[i][j]
        #         elif j == n - 1:
        #             dp[i][j] = min(matrix[i - 1][j], matrix[i - 1][j - 1]) + matrix[i][j]
        #         else:
        #             dp[i][j] = min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i - 1][j + 1]) + matrix[i][j]
        # return min(dp[n - 1])

        n = len(matrix)
        dp = copy.deepcopy(matrix[0])
        for i in range(1, n):
            for j in range(n):
                if j == 0:
                    pre = dp[j]
                    dp[j] = min(dp[j], dp[j + 1]) + matrix[i][j]
                elif j == n - 1:
                    dp[j] = min(dp[j], pre) + matrix[i][j]
                else:
                    cur = dp[j]
                    dp[j] = min(pre, dp[j], dp[j + 1]) + matrix[i][j]
                    pre = cur
        return min(dp)


word1 = 'horse'
word2 = 'ros'
solve = Solution()
print(solve.minDistance(word1, word2))

matrix = [[-19, 57], [-40, -5]]
print(solve.minFallingPathSum(matrix))
