'''
5.最长回文子串
647.回文子串
516.最长回文子序列
'''


class Solution:
    # 返回回文子串的数目
    def countSubstrings(self, s: str) -> int:
        # # dp[i][j] [i,j]区间内的子串是否是回文子串
        # # if s[i]==s[j] 有三种情况：
        # # 1 i == j 只有一个字符，True
        # # 2 i+1 == j 两个字符 True
        # # 3 i+1 < j 三个或三个以上字符取决于 dp[i+1][j-1]
        # n = len(s)
        # res = 0
        # dp = [[False] * n for _ in range(n)]
        # for i in range(n - 1, -1, -1):  # 从后往前 因为dp[i][j]和dp[i+1][j-1]有关
        #     for j in range(i, n):
        #         if s[i] == s[j]:
        #             if i == j or i + 1 == j:
        #                 res += 1
        #                 dp[i][j] = True
        #             elif dp[i + 1][j - 1]:
        #                 res += 1
        #                 dp[i][j] = True
        # return res

        # 双指针法
        def calc_palindrome(i: int, j: int) -> int:
            cnt = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
                cnt += 1
            return cnt

        n = len(s)
        res = 0
        for i in range(n):
            res += calc_palindrome(i, i)  # 中心点有一个
            res += calc_palindrome(i, i + 1)  # 有两个
        return res

    # 最长回文子序列
    def longestPalindromeSubseq(self, s: str) -> int:
        # dp[i][j] [i,j]区间内去最长回文子序列的长度
        # 关键看s[i] s[j]是否相同 dp[i][j]=dp[i+1][j-1]+2
        # 不相同说明s[i] s[j]的同时加入不能增加回文子序列的长度 那么分别加入
        # dp[i][j]=max(dp[i][j-1], dp[i+1][j])
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        # base case 其他情况都是0
        for i in range(n):
            dp[i][i] = 1
        # 从后往前 从左往右
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        return dp[0][n - 1]

    def longestPalindrome(self, s: str) -> str:
        # dp[i][j] [i,j]区间内的子串是否回文
        # s[i]==s[j] dp[i][j]是否回文取决于dp[i+1][j-1] 还要考虑2个字符的情况
        # 若不等，dp[i][j]=False

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        dis = 0
        record = [0] * 2
        # base case
        for i in range(n):
            dp[i][i] = True
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if i + 1 == j:  # 只有2个字符
                        dp[i][j] = True
                        if dis < j - i + 1:
                            dis = j - i + 1
                            record[0], record[1] = i, j
                    elif dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if dis < j - i + 1:
                            dis = j - i + 1
                            record[0], record[1] = i, j
        return s[record[0]: record[1] + 1]