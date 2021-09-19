'''
滑动窗口
209.长度最小的子数组
904.水果成篮
76.最小覆盖子串
'''
from typing import List
import collections


class Solution:
    # 和为target的最短子数组
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')  # 最小窗口长度
        i = 0  # 窗口左端
        sum = 0  # 窗口之和
        n = len(nums)
        for j in range(n):
            sum += nums[j]
            while sum >= target:  # 窗口之和>=target时移动窗口左端
                res = min(res, j - i + 1)  # 记录最小窗口长度
                sum -= nums[i]
                i += 1
        # 如果一直没有记录最下窗口长度，说明窗口和不足target
        return res if res != float('inf') else 0

    # 只包含2种元素的最长子数组
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0  # 最大窗口长度
        i = 0  # 窗口左端
        count = collections.Counter()  # {水果类型:水果个数}
        n = len(fruits)
        for j in range(n):
            count[fruits[j]] += 1
            while len(count) > 2:  # 水果类型超过2 没篮子放了
                count[fruits[i]] -= 1
                if count[fruits[i]] == 0:
                    count.pop(fruits[i])  # 删掉该水果
                i += 1
            res = max(res, j - i + 1)  # 窗口大小 j-i+1

        return res




solve = Solution()
# print(solve.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
print(solve.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
