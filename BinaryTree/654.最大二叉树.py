'''
构造二叉树相关
654.最大二叉树
105.从前序和中序遍历序列构造二叉树
106.从中序和后序遍历序列构造二叉树
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # 返回构建出树的root
        if not nums:
            return None
        max_index = nums.index(max(nums))
        left = nums[:max_index]
        right = nums[max_index + 1:]

        root = TreeNode(nums[max_index])
        root.left = self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 搞清 root 左子树 右子树在两个数组中的位置
        if not preorder and not inorder:
            return None

        root = TreeNode(preorder[0])
        root_in_index = inorder.index(root.val)

        left_in = inorder[:root_in_index]
        left_size = len(left_in)
        left_pre = preorder[1:1 + left_size]

        right_in = inorder[root_in_index + 1:]
        right_pre = preorder[1 + left_size:]

        root.left = self.buildTree(left_pre, left_in)
        root.right = self.buildTree(right_pre, right_in)

        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # 搞清 root 左子树 右子树 在两个数组中的位置
        if not inorder and not postorder:
            return None

        root = TreeNode(postorder[-1])
        root_in_index = inorder.index(root.val)

        left_in = inorder[:root_in_index]
        left_size = len(left_in)
        left_post = postorder[:left_size]

        right_in = inorder[root_in_index + 1:]
        right_post = postorder[left_size:-1]

        root.left = self.buildTree(left_in, left_post)
        root.right = self.buildTree(right_in, right_post)

        return root


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    # root
    root = preorder[0]
    rootidx = inorder.index(root)
    leftin = inorder[:rootidx]
    left_size = len(leftin)
    leftpre = preorder[1:1 + left_size]
    rightin = inorder[rootidx + 1:]
    rightpre = preorder[1 + left_size:]
    print(rootidx)
    print(leftin)
    print(rightin)
    print(leftpre)
    print(rightpre)
