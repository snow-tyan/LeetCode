'''
279.完全平方数
bfs+dp+贪心
'''

import math


class Solution:
    # DP
    def numSquaresDP(self, n: int) -> int:
        # 转换为完全背包
        # 给定1,4,9,16,... 求组成n的最小数量，每个数字无限次
        store = [i ** 2 for i in range(1, 1 + int(math.sqrt(n)))]
        # print(store)
        m = len(store)
        dp = [10000] * (n + 1)
        # base case
        dp[0] = 0
        for i in range(m):
            # store[i]=(i+1)**2
            for j in range(store[i], n + 1):
                dp[j] = min(dp[j], dp[j - store[i]] + 1)
        return dp[n]

    # BFS
    def numSquaresBFS(self, n: int) -> int:
        # BFS像一层一层拆解n，最终返回的是树的level
        store = [i ** 2 for i in range(1, 1 + int(math.sqrt(n)))]
        queue = [n]
        visited = {n: 1}  # key是拆解出来的数，val是level。初始1层
        while queue:
            val = queue.pop(0)
            if val in store:
                return visited[val]
            for sq in store:
                if val - sq > 0 and val - sq not in visited:
                    queue.append(val - sq)
                    visited[val - sq] = visited[val] + 1
        return -1  # 理论上一个整数必可以分为至多4个数平方和

    # 贪心
    def numSquaresGREED(self, n: int) -> int:
        # 可证count=1,2,3,4 因状态有限，故可以用贪心
        # 每个数字都贪心的尝试 自己是1个数的平方？2个？3个？
        store = [i ** 2 for i in range(1, 1 + int(math.sqrt(n)))]

        # 数字n能否被划分为count个数的平方和
        def divisible(n: int, count: int) -> bool:
            if count == 1:
                return n in store

            for sq in store:
                if divisible(n - sq, count - 1):
                    return True
            return False

        for count in range(1, n + 1):
            if divisible(n, count):
                return count
        return -1


solve = Solution()
n = 13
print(solve.numSquaresDP(n))
print(solve.numSquaresBFS(n))
print(solve.numSquaresGREED(n))
