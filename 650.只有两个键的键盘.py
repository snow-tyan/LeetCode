'''
9.19 每日一题
650.只有两个键的键盘
'''


class Solution:
    def minSteps(self, n: int) -> int:
        # dp[1]=0  dp[2]=2  dp[3]=3  dp[4]=dp[2]+2  dp[5]=5
        # dp[6]=dp[3]+2  dp[8]=dp[4]+2  dp[9]==dp[3]+3
        # 质因数分解
        if n == 1:
            return 0
        for i in range(2, n):
            if n % i == 0:
                return i + self.minSteps(n // i)  # 套娃开始

        return n

    def minStepsDP(self, n: int) -> int:
        # dp[i] 打印i个A最少操作次数
        # 由j个A 复制+若干次粘贴 dp[i]=dp[j]+i//j 或 dp[i//j]+j (i%j==0)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = float('inf')
            j = 1
            # i的因数j和i/j，必有一个<=√i 优化 只在[1, √i]范围内枚举
            while j * j <= i:  # 枚举j
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j, dp[i // j] + j)
                j += 1

        return dp[n]


solve = Solution()
print(solve.minSteps(12))
print(solve.minStepsDP(12))
