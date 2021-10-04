'''
每日一题 8.29
1588.所有奇数长度子数组之和
'''

from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum = 0
        subsize = 1
        # 每种长度 1 3 5 ...
        while subsize <= len(arr):
            # 各长度子数组之和
            for i in range(len(arr) - subsize + 1):
                subsum = 0
                # 各长度子数组值
                for j in range(subsize):
                    subsum += arr[i + j]
                sum += subsum
            subsize += 2

        return sum

    def sumOddPrefix(self, arr: List[int]) -> int:
        sum = 0
        subsize = 1
        presum = [0]
        # 前缀和数组
        for i in range(len(arr)):
            presum.append(presum[i] + arr[i])

        # 每种长度 1 3 5 ...
        while subsize <= len(arr):
            # 各长度子数组之和
            for i in range(len(arr) - subsize + 1):
                # 各长度子数组值
                sum += presum[i + subsize] - presum[i]
            subsize += 2

        return sum


if __name__ == '__main__':
    arr = [1, 4, 2, 5, 3]
    solve = Solution()
    print(solve.sumOddLengthSubarrays(arr))
    print(solve.sumOddPrefix(arr))