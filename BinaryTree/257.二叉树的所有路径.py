'''
257.二叉树的所有路径
404.左叶子之和
513.找树左下角的值
112.路径总和
113.路径总和II
617.合并二叉树
'''
from typing import List, Optional
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def backtracking(root: TreeNode) -> None:
            path.append(str(root.val))
            if not root.left and not root.right:  # 叶子节点
                res.append('->'.join(path))
                return
            if root.left:
                backtracking(root.left)
                path.pop()  # 回溯
            if root.right:
                backtracking(root.right)
                path.pop()

        res = []
        path = []
        backtracking(root)
        return res

    def sumOfLeftLeavesIter(self, root: TreeNode) -> int:
        # 检查当前节点的左孩子是不是左叶子
        def check(root: TreeNode) -> bool:
            if root.left and not root.left.left and not root.left.right:
                return True
            return False

        if not root:
            return 0
        res = 0
        queue = collections.deque([root])
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.pop()
                if node.left:
                    if check(node):
                        res += node.left.val
                    else:
                        queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # 检查当前节点的左孩子是不是左叶子
        def check(root: TreeNode) -> bool:
            if root.left and not root.left.left and not root.left.right:
                return True
            return False

        res = 0
        if check(root):
            res += root.left.val
        return res + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

    def findBottomLeftValue(self, root: TreeNode) -> int:
        # 层序遍历最简单，返回最后一层第一个元素 略

        # 递归 找最深一层的叶子节点，前序遍历优先搜索左
        def backtracking(root: TreeNode, depth: int) -> None:
            nonlocal max_depth, res
            if not root.left and not root.right:
                if depth > max_depth:
                    max_depth = depth
                    res = root.val
                return
            if root.left:
                depth += 1
                backtracking(root.left, depth)
                depth -= 1
            if root.right:
                depth += 1
                backtracking(root.right, depth)
                depth -= 1

        max_depth = float('-inf')
        res = 0
        backtracking(root, 0)
        return res

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 深搜 回溯 找到即返回True
        def backtracking(root: Optional[TreeNode], path_sum: int) -> bool:
            if not root.left and not root.right:  # 叶子节点
                if path_sum == targetSum:
                    return True
                return False

            if root.left:
                path_sum += root.left.val
                if backtracking(root.left, path_sum):
                    return True
                path_sum -= root.left.val
            if root.right:
                path_sum += root.right.val
                if backtracking(root.right, path_sum):
                    return True
                path_sum -= root.right.val

            return False

        if not root:
            return False
        return backtracking(root, root.val)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # 递归 回溯 找到一条即可返回 递归函数需要返回bool
        # 找所有满足要求的路径 无需返回值，暴力搜索
        def backtracking(root: Optional[TreeNode], path_sum: int) -> None:
            if not root.left and not root.right:
                if path_sum == targetSum:
                    # 该路径加入答案
                    res.append(path[:])
                return

            if root.left:
                path_sum += root.left.val
                path.append(root.left.val)
                backtracking(root.left, path_sum)
                path_sum -= root.left.val
                path.pop()
            if root.right:
                path_sum += root.right.val
                path.append(root.right.val)
                backtracking(root.right, path_sum)
                path_sum -= root.right.val
                path.pop()

        if not root:
            return []
        res = []
        path = [root.val]
        backtracking(root, root.val)
        return res

    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1

        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1

    def mergeTreesIter(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1

        queue = collections.deque([root1, root2])
        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()
            node1.val += node2.val
            if node1.left and node2.left:  # 都有左孩子
                queue.append(node1.left)
                queue.append(node2.left)

            if node1.right and node2.right:  # 都有右孩子
                queue.append(node1.right)
                queue.append(node2.right)

            if not node1.left:  # node1 缺少左右孩子，直接赋值
                node1.left = node2.left

            if not node1.right:
                node1.right = node2.right

        return root1