'''
10.2
第62场双周赛
A.将一维数组转变成二维数组         easy
B.连接后等于目标字符串的字符串对    medium
C.考试的最大困扰度               medium
    1004.最大连续1的个数III      滑窗
D.分割数组的最多方案数            hard
'''
from typing import List
import collections


class Solution:
    # 把一维数组original转变成m*n的二维数组
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        res = []
        for i in range(m):
            res.append(original[i * n:(i + 1) * n])
        return res

    # 返回满足nums[i]+nums[j]=target (i!=j)的数目
    # 这不就是两数之和吗
    def numOfPairs(self, nums: List[str], target: str) -> int:
        # # 暴力枚举 O(n^2)
        # n = len(nums)
        # cnt = 0
        # for i in range(n):
        #     for j in range(n):
        #         # i==j直接略过 不等长也略过
        #         if i != j and len(nums[i]) + len(nums[j]) == len(target) and nums[i] + nums[j] == target:
        #             cnt += 1
        # return cnt

        # 哈希 O(n)
        # 遍历字符串数组 逐个判断是否是target的前缀或后缀，并对后缀长度计数
        n, t = len(nums), len(target)
        pre, suf = [False] * n, [False] * n  # 是否为target前后缀
        suf_mp = collections.Counter()  # 若是target后缀，对其长度计数
        cnt = 0
        for i in range(n):
            m = len(nums[i])
            if m > t:
                continue
            if nums[i] == target[:m]:  # 前缀
                pre[i] = True
            if nums[i] == target[t - m:]:  # 后缀 target[-m:]
                suf[i] = True
                suf_mp[m] += 1  # 长度为m的后缀数目+1
        for i in range(n):
            if pre[i]:
                cnt += suf_mp[t - len(nums[i])]
                # 除去自身即是前缀亦为后缀的重复计数
                if suf[i] and len(nums[i]) * 2 == t:
                    cnt -= 1
        return cnt

    # 老师想增加学生对答案的不确定性，最大化连续相同答案，最多操作k次
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # 贪心解法 吴自华
        T, F = [-1], [-1]  # 记录T,F的下标 头加上-1 尾加上n
        n = len(answerKey)
        for i in range(n):
            if answerKey[i] == 'T':
                T.append(i)
            else:
                F.append(i)
        T.append(n)
        F.append(n)
        # k大于T或者F的个数，可以全部连续
        if k >= len(T) - 2 or k >= len(F) - 2:
            return n

        res = 0
        # 连续F
        for i in range(1, len(T) - k):
            # T[i+k]第k个T
            # T[i-1]第-1个T
            # T[i+k]-T[i-1]-1 此区域的T全改成F可得F的最大连续长度
            res = max(res, T[i + k] - T[i - 1] - 1)
        # 连续T
        for i in range(1, len(F) - k):
            res = max(res, F[i + k] - F[i - 1] - 1)
        return res

    # Problem C 滑窗解
    def maxConsecutiveAnswers_SW(self, answerKey: str, k: int) -> int:
        # 滑窗
        # 记录窗口内最大连续T/F的个数
        def sliding_window(answerKey: str, k: int, ch: str) -> int:
            n = len(answerKey)
            left, right, cnt = 0, 0, 0  # cnt记录T/F的个数
            res = 0
            while right < n:
                # 窗口右
                while right < n and cnt <= k:
                    if answerKey[right] == ch:
                        cnt += 1
                    right += 1
                    if cnt <= k:
                        res = max(res, right - left)
                # 窗口左
                while left <= right and cnt > k:
                    if answerKey[left] == ch:
                        cnt -= 1
                    left += 1
            return res

        res = 0
        res = max(res, sliding_window(answerKey, k, 'T'), sliding_window(answerKey, k, 'F'))
        return res

    # 双哈希表
    def waysToPartition(self, nums: List[int], k: int) -> int:
        # 1 不改动原数组的情况，则等同于前缀和数组S中总和T的一半的出现次数; 即presum[n]//2
        # 2 改动一个元素的情况。枚举需要修改的位置
        #   假定修改了第i个元素，那么前i-1个前缀和不变，之后的每个前缀和要增加d = k-nums[i]
        #   因此合法分割，i左侧的前缀和需要=presum[n]//2 + d//2 右侧=presum[n]//2 - d//2
        #   用两个哈希表动态维护i左右前缀和的个数
        n = len(nums)
        pre_sum = [0] * (n + 1)
        cnt = 0
        mpl, mpr = collections.Counter(), collections.Counter()
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]
        for i in range(1, n):
            mpr[pre_sum[i]] += 1
        # 不改变
        if pre_sum[n] % 2 == 0:
            cnt = mpr[pre_sum[n] // 2]
        for i in range(1, n + 1):
            d = k - nums[i - 1]
            if (pre_sum[n] + d) % 2 == 0:
                cnt = max(cnt, mpl[(pre_sum[n] + d) // 2] + mpr[(pre_sum[n] - d) // 2])
            mpl[pre_sum[i]] += 1
            mpr[pre_sum[i]] -= 1
        return cnt


solve = Solution()
# print(solve.construct2DArray(original=[1, 2, 3, 4], m=2, n=2))
# print(solve.numOfPairs(nums=["1", "1", "1"], target="11"))
print(solve.maxConsecutiveAnswers(answerKey="TTFTTFTTF", k=2))
print(solve.maxConsecutiveAnswers_SW(answerKey="TTFTTFTTF", k=2))
