'''
每日一题 9.4
剑指offer10.斐波那契数列

无非递归、动规 O(N)
矩阵快速幂 O(logN) 看不懂？
'''


class Solution:
    def fib(self, n: int) -> int:
        # if n == 0 or n == 1:
        #     return n
        # return self.fib(n - 1) + self.fib(n - 2)

        # 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
        if n == 0 or n == 1:
            return n

        f0, f1 = 0, 1
        for _ in range(n - 1):
            fn = int((f0 + f1) % (1e9 + 7))
            f0 = f1
            f1 = fn
        return fn
