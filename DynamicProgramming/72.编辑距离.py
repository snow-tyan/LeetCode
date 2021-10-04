'''
72.编辑距离
392.判断子序列
115.不同的子序列
583.两个字符串的删除操作
931.下降路径最小和
'''
from typing import List


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
        n = len(matrix)
        dp = matrix.copy()
        for i in range(1, n):
            for j in range(n):
                if j == 0:
                    dp[i][j] = min(matrix[i - 1][j], matrix[i - 1][j + 1]) + matrix[i][j]
                elif j == n - 1:
                    dp[i][j] = min(matrix[i - 1][j], matrix[i - 1][j - 1]) + matrix[i][j]
                else:
                    dp[i][j] = min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i - 1][j + 1]) + matrix[i][j]
        return min(dp[n - 1])

    def isSubsequence(self, s: str, t: str) -> bool:
        # # 双指针，遍历s和t串 O(m+n)
        # i, j = 0, 0
        # while i < len(s) and j < len(t):
        #     if s[i] == t[j]:
        #         i += 1
        #         j += 1
        #     else:
        #         j += 1
        # return True if i == len(s) else False

        # # 编辑距离 删除t
        # # dp[i][j] [0,i-1]的s和[0,j-1]的t，相同子序列的长度
        # m, n = len(s), len(t)
        # dp = [[0] * (n + 1) for _ in range(m + 1)]
        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         if s[i - 1] == t[j - 1]:
        #             dp[i][j] = dp[i - 1][j - 1] + 1
        #         else:
        #             dp[i][j] = dp[i][j - 1]  # 编辑距离中的删操作
        # return True if dp[m][n] == len(s) else False

        # 进阶：如果大量S来匹配T，怎么办？
        # 把T做成一个表，m行26列，记录每个字符第一次出现的位置
        # dp[i][j] 到T的第i个位置为止，其后j个字符出现的第一个位置
        # dp[i][j] = i (T[i]==j) dp[i][j] = dp[i+1][j]
        def make_dp(t: str) -> List[List[int]]:
            m = len(t);
            dp = [[0] * 26 for _ in range(m + 1)]
            for i in range(26):
                dp[m][i] = -1
            for i in range(m - 1, -1, -1):
                for j in range(26):
                    if ord(t[i]) == j + ord('a'):
                        dp[i][j] = i
                    else:
                        dp[i][j] = dp[i + 1][j]
            return dp

        def match(s: str, dp: List[List[int]]) -> bool:
            n = len(s)
            index = 0
            for i in range(n):
                index = dp[index][ord(s[i]) - ord('a')]
                if index == -1:
                    return False
                index += 1
            return True

        dp = make_dp(t)
        return match(s, dp)

    def numDistinct(self, s: str, t: str) -> int:
        # 编辑距离 删除s中的元素，使之成为t
        # dp[i][j] [0,i-1]的s中出现[0,j-1]的t的子序列序列的个数
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[m][n]


word1 = 'horse'
word2 = 'ros'
solve = Solution()
print(solve.minDistance(word1, word2))

matrix = [[-19, 57], [-40, -5]]
print(solve.minFallingPathSum(matrix))
