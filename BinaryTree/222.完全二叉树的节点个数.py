'''
222.完全二叉树的节点个数

普通二叉树的节点个数: 遍历一遍O(N)
满二叉树的节点个数: 求出高度h，公式2^h-1 求高度O(logN)
'''
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_h, right_h = 0, 0
        # 计算高度，遍历 O(logN)
        temp = root
        while temp.left:
            temp = temp.left
            left_h += 1
        temp = root
        while temp.right:
            temp = temp.right
            right_h += 1

        # 满二叉树
        if left_h == right_h:
            return int(math.pow(2, left_h + 1)) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)  # 还是用了递归，空间复杂度
