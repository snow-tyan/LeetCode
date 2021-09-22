'''
111.二叉树的最小深度
104.二叉树的最大深度
'''
from collections import deque


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
        que = deque([root])
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
        queue = deque([root])
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
    print(solve.minDepthDFS(root1))
    print(solve.minDepthDFS(root2))
    print(solve.minDepthBFS(root1))
    print(solve.minDepthBFS(root2))
