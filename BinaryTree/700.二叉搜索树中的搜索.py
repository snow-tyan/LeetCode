'''
BST
700.二叉搜索树中的搜索
530. 二叉搜索树的最小绝对差 783.二叉搜索树节点最小距离
501. 二叉搜索树中的众数
236.二叉树的最近公共祖先
235.二叉搜索树的最近公共祖先
'''
from typing import List
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return root

        if root.val == val:
            return root
        # val 大于 root， 则在左子树
        elif root.val > val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)

    # 这迭代，不借队列不借栈
    def searchBSTIter(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return None

    def getMinimumDifference(self, root: TreeNode) -> int:
        # 中序遍历 升序 后-前算最小值
        # 维护前一个节点-当前节点
        def traversal(root: TreeNode) -> None:
            nonlocal min_diff, pre
            if not root:
                return

            traversal(root.left)
            if pre and min_diff > root.val - pre.val:
                min_diff = root.val - pre.val
            pre = root
            traversal(root.right)

        min_diff = float('inf')
        pre = None
        traversal(root)
        return min_diff

    def findMode(self, root: TreeNode) -> List[int]:
        # 最简单的做法，遍历树，统计频率、排序
        # 方法二：遍历两遍BST 第一遍找最大频率 第二遍找=最大频率的所有节点值
        # 方法三：遍历一遍BST 边找边放入结果，如果出现更大频率，清空结果集再放入
        def traversal(root: TreeNode) -> None:
            nonlocal count, max_count, pre
            if not root:
                return
            # 中序遍历
            traversal(root.left)
            if not pre:  # 最左端孩子
                count = 1
            elif pre.val == root.val:
                count += 1
            else:
                count = 1
            pre = root

            if max_count == count:
                res.append(pre.val)
            if max_count < count:
                max_count = count
                res.clear()
                res.append(root.val)

            traversal(root.right)

        res = []
        count = 0
        max_count = 0
        pre = None
        traversal(root)
        return res

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 后序遍历 天然回溯
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
        # if not right:
        return left

    def lowestCommonAncestorBST(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestorBST(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestorBST(root.right, p, q)
        return root

    def lowestCommonAncestorBSTIter(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
        return None
