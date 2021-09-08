# 后序遍历

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # p,q 都在root为根节点的树中，函数返回LCA
        # p,q 有一个在，返回其本身(p或q)
        # p,q 都不在，返回None
        if not root:
            return root
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 左右子树均返回非空，那么p，q必分散在左右子树
        if left and right:
            return root

        # 左子树空，则p，q必在右子树
        if not left:
            return right
        # 反之
        if not right:
            return left
