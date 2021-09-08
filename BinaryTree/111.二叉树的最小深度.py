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
        if not root:
            return 0
        que = deque([(root, 1)])
        while que:
            node, dep = que.popleft()
            # 叶子节点，返回
            if not node.left and not node.right:
                return dep
            if node.left:
                que.append((node.left, dep + 1))
            if node.right:
                que.append((node.right, dep + 1))
        return 0


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
