'''
1373.二叉搜索子树最大键值和
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        # 1 左右子树是否是BST
        # 2 如果是，加上root还是不是BST(左子树最大值，右子树最小值)
        # 3 如果满足，自身键值和 vs 左 vs 右子树键值和
        self.maxsum = 0

        # 返回值
        # 1 该树是否是BST
        # 2 该树的最小值
        # 3 该树的最大值
        # 4 该树的键值和
        def traverse(root: TreeNode) -> List:
            if not root:
                return [True, 4e4, -4e4, 0]

            left = traverse(root.left)
            right = traverse(root.right)

            # 该树是不是BST
            # 若不是就不用算了
            if not left[0] or not right[0] or root.val <= left[2] or root.val >= right[1]:
                return [False, 0, 0, 0]

            curmin = root.val if root.val < left[1] else left[1]
            curmax = root.val if root.val > right[2] else right[2]
            sum = left[3] + right[3] + root.val
            self.maxsum = max(self.maxsum, sum)

            return [True, curmin, curmax, sum]

        traverse(root)
        return self.maxsum
