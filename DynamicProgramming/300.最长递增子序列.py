'''
# 子序列问题
子序列 不连续；子数组 连续
300.最长递增子序列
673.最长递增子序列的个数
674.最长连续递增序列
718.最长重复子数组
1143.最长公共子序列
不相交的线
最大子序和
判断子序和
不同的子序列
回文子串
最长回文子序列
'''
from typing import List


class Solution:
    # 最长递增子序列的长度
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] 第i位置之前的最长递增子序列长度
        # dp[i]=位置j从0到i-1各个位置的最长递增子序列长度+1的最大值
        n = len(nums)
        if n == 0:
            return 0
        dp = [1] * n
        # base case
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)  # i之前的最长递增子序列长度+1
        return max(dp)

    # 最长递增子序列的个数
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # dp[i] 以第i个数结尾的最长递增子序列的长度
        # cnt[i] 以第i个数结尾的最长递增子序列的个数
        n = len(nums)
        if n == 0:
            return 0
        dp = [1] * n
        cnt = [1] * n
        # base case
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:  # 找到了一个更长的递增子序列
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    elif dp[j] + 1 == dp[i]:  # 找到了两条长度相同递增子序列
                        cnt[i] += cnt[j]
        max_length = max(dp)
        res = 0
        for i in range(n):
            if dp[i] == max_length:
                res += cnt[i]
        return res

    # 最长连续递增子序列
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
        return max(dp)

    # 最长公共子数组
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # dp[i][j] 以A下标i-1结尾，B下标j-1结尾的公共最长子数组长度
        n, m = len(nums1), len(nums2)
        res = 0
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        # base case
        for i in range(1, n + 1):
            for j in range(1, m + 1):  # 搜索nums2
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                res = max(res, dp[i][j])
        return res

    # 最长公共子序列