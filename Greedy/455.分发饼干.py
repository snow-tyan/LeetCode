'''
455.分发饼干
135.分发糖果
406.根据身高重建队列
376.摆动序列
53.最大子序和 dp+贪心
122.买卖股票最佳时机II
738.单调递增的数字
968.监控二叉树
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # g[i]胃口值 s[j]饼干尺寸 s[j]>=g[i]即得到满足
        # 优先考虑饼干 小饼干喂饱小胃口
        # 也可以优先考虑胃口，大饼干喂饱大胃口
        g.sort()
        s.sort()  # 饼干
        i, j = 0, 0
        cnt = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:  # 满足了一个小孩
                cnt += 1
                i += 1
            j += 1
        return cnt

    def candy(self, ratings: List[int]) -> int:
        # 每人至少分一个
        # 评分高的孩子必须比两侧孩子分的多
        # 贪心策略：先保证右比左大分的多，再考虑左比右大
        n = len(ratings)
        candy = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1  # 比左边分的多1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)  # 局部最优
        return sum(candy)

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 遇到两个维度的，先确定一个维度 比如135.分发糖果
        # 按hi降序 ki升序
        people.sort(key=lambda x: (-x[0], x[1]))
        # print(people)
        # 按ki作为下标插入
        que = []
        for p in people:
            que.insert(p[1], p)  # list.insert(index, obj)

        return que

    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 实际上是统计数组的峰和谷的个数哦
        n = len(nums)
        if n < 2:
            return n

        cnt = 1
        pre_diff, cur_diff = 0, 0
        for i in range(1, n):
            cur_diff = nums[i] - nums[i - 1]
            # 只有数组最左侧才会出现pre_diff==0的情况
            if pre_diff >= 0 and cur_diff < 0 or pre_diff <= 0 and cur_diff > 0:
                cnt += 1
                pre_diff = cur_diff
        return cnt

    def maxSubArray(self, nums: List[int]) -> int:
        # 这是一道dp题，但也能用贪心做
        # 连续子序和最大，当连续和为负数时立即重新计算连续和
        # 因为负数+下一个数<下一个数
        max_sum = float('-inf')
        cur_sum = 0
        for num in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += num
            max_sum = max(max_sum, cur_sum)
        return max_sum

    def maxProfit(self, prices: List[int]) -> int:
        # 实际上就是底点买入，高点卖出
        # 求差分数组，正的就表示买卖
        res = 0
        n = len(prices)
        for i in range(1, n):
            res += max((prices[i] - prices[i - 1]), 0)
        return res

    def monotoneIncreasingDigits(self, n: int) -> int:
        # # 检查各位是否单调递增 TLE
        # def checkmono(num: int) -> bool:
        #     pre = 10
        #     while num:
        #         cur = num % 10
        #         if cur > pre:
        #             return False
        #         pre = cur
        #         num //= 10
        #     return True
        #
        # for i in range(n, -1, -1):
        #     if checkmono(i):
        #         return i
        # return 0

        # 贪心
        # 若s[i-1]>s[i] 让s[i-1]--,然后s[i]置为9 局部最优
        nums = list(str(n))  # python 字符串不可更改，转list
        for i in range(len(nums) - 1, 0, -1):
            if int(nums[i - 1]) > int(nums[i]):
                nums[i - 1] = str(int(nums[i - 1]) - 1)
                nums[i:] = '9' * (len(nums) - i)
        return int(''.join(nums))

    def minCameraCover(self, root: TreeNode) -> int:
        # 0 无覆盖 1 有摄像头 2 有覆盖
        def traversal(root: TreeNode) -> int:
            nonlocal res
            if not root:  # 空节点默认有覆盖，因为要使摄像头数目最小
                return 2

            left = traversal(root.left)
            right = traversal(root.right)

            # 左右孩子都有覆盖
            if left == 2 and right == 2:
                return 0
            # 左右孩子有一个无覆盖
            elif left == 0 or right == 0:
                res += 1
                return 1
            # 左右有一个安装了摄像头
            elif left == 1 or right == 1:
                return 2
            return -1

        res = 0
        if traversal(root) == 0:  # root无覆盖
            res += 1
        return res
