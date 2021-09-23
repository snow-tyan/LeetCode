'''
111.二叉树的最小深度
104.二叉树的最大深度
100.相同的树
101.对称二叉树 与100及其相似
572. 另一棵树的子树
110.平衡二叉树 判断是否是高度上达到平衡的二叉树
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
    # 深搜，记录最小深度
    def minDepthDFS(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        min_dep = 1e5
        if root.left:
            min_dep = min(self.minDepthDFS(root.left), min_dep)
        if root.right:
            min_dep = min(self.minDepthDFS(root.right), min_dep)

        return min_dep + 1

    # 广搜，遍历到叶子节点时即可返回
    def minDepthBFS(self, root: TreeNode) -> int:
        # 广搜，遍历到叶子节点 停
        if not root:
            return 0
        que = collections.deque([root])
        depth = 0
        while que:
            n = len(que)
            depth += 1
            for _ in range(n):
                node = que.popleft()
                # 叶子节点，返回
                if not node.left and not node.right:
                    return depth
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return 0

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = collections.deque([root])
        depth = 0
        while queue:
            n = len(queue)
            depth += 1
            for _ in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def check(p: TreeNode, q: TreeNode) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and check(p.left, q.left) and check(p.right, q.right)

        return check(p, q)

    def isSymmetric(self, root: TreeNode) -> bool:
        # 是否对称
        # 一个二叉树是否对称 1 根节点值是否相等 2 左子树右子树是否对称 -- 递归
        # 通过两个指针p q实现 p左q右 p右q左
        def check(p: TreeNode, q: TreeNode) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and check(p.left, q.right) and check(p.right, q.left)

        return check(root, root)

    def isSymmetricIter(self, root: TreeNode) -> bool:
        # 层序遍历
        # 将两个root入队 每次pop两个节点比较
        # 然后将每个节点左右孩子 按 相反 顺序入队
        queue = collections.deque([root, root])
        while queue:
            u = queue.popleft()
            v = queue.popleft()
            if not u and not v:
                continue
            if not u or not v or u.val != v.val:
                return False
            queue.append(u.left)
            queue.append(v.right)
            queue.append(u.right)
            queue.append(v.left)
        return True

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # is same tree
        def check(p: TreeNode, q: TreeNode) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and check(p.left, q.left) and check(p.right, q.right)

        if not root:  # 递归只有root在变
            return False
        return check(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isBalanced(self, root: TreeNode) -> bool:
        def getHeight(root: TreeNode) -> int:
            if not root:
                return 0
            l_h = getHeight(root.left)
            if l_h == -1:
                return -1
            r_h = getHeight(root.right)
            if r_h == -1:
                return -1
            # 当前节点的高度 1 + max(l_h, r_h)
            return 1 + max(l_h, r_h) if -2 < l_h - r_h < 2 else -1

        return True if getHeight(root) != -1 else False


if __name__ == '__main__':
    root1 = TreeNode(3)
    a = TreeNode(9)
    b = TreeNode(20)
    c = TreeNode(15)
    d = TreeNode(7)
    root1.left = a
    root1.right = b
    b.left = c
    b.right = d

    root2 = TreeNode(1)
    e = TreeNode(2)
    root2.left = e

    solve = Solution()
    # print(solve.minDepthDFS(root1))
    # print(solve.minDepthDFS(root2))
    # print(solve.minDepthBFS(root1))
    # print(solve.minDepthBFS(root2))
