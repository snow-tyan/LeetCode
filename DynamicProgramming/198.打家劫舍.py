'''
198.打家劫舍
213.打家劫舍II
337.打家劫舍III
'''
from typing import List, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i]走到第i家房屋时能偷到的最大金额
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[n - 1]

    def robII(self, nums: List[int]) -> int:
        # 房屋连成了环
        # 不考虑首元素或尾元素就和打家劫舍一样了
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        dp = [0] * n
        dp[1] = nums[1]
        dp[2] = max(nums[1], nums[2])
        for i in range(3, n):  # 不考虑首元素
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        dp_pop_first = dp[n - 1]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n - 1):  # 不考虑尾元素
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        dp_pop_tail = dp[n - 2]
        return max(dp_pop_first, dp_pop_tail)  # 求最大

    def robIII(self, root: TreeNode) -> int:
        # 数组房屋换成了棵树
        # 返回长度2的数组 0：不偷 1 偷
        # 数值代表 偷/不偷 所能盗取最高金额
        def traversal(root: TreeNode) -> List[int]:
            if not root:
                return [0, 0]
            # 返回子树 偷/不偷 所能盗取最高金额
            left = traversal(root.left)
            right = traversal(root.right)
            tou = root.val + left[0] + right[0]  # 偷root 左右孩子就不能偷
            butou = max(left) + max(right)  # 不偷root 左右孩子可偷可不偷，返回最大的
            return [butou, tou]

        return max(traversal(root))

