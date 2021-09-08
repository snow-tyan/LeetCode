'''
1
226.翻转二叉树
114.二叉树拉平成链表
116.填充每个节点的右侧next指针
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 交换每个节点的左右孩子
        if not root:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left

        return root

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 1 左右子树拉平（递归）
        # 2 存下右子树，左子树作为右子树
        # 3 右子树接到右，root左子树置空
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        temp = TreeNode()
        temp.right = root.right

        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = temp.right


    def connect(self, root: 'Node') -> 'Node':
        def connectTwoNode(node1: 'Node', node2: 'Node') -> None:
            if not node1 and not node2:
                return
            node1.next = node2

            connectTwoNode(node1.left, node1.right)
            connectTwoNode(node2.left, node2.right)
            connectTwoNode(node1.right, node2.left)

        if not root:
            return root
        connectTwoNode(root.left, root.right)
        return root