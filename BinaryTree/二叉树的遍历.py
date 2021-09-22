'''
再次练习二叉树的遍历
递归+非递归
144.二叉树的前序遍历
94.二叉树的中序遍历
145.二叉树的后序遍历
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Recur:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def traversal(root: TreeNode) -> None:
            if not root:
                return
            res.append(root.val)
            traversal(root.left)
            traversal(root.right)

        res = []
        traversal(root)
        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def traversal(root: TreeNode) -> None:
            if not root:
                return
            traversal(root.left)
            res.append(root.val)
            traversal(root.right)

        res = []
        traversal(root)
        return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def traversal(root: TreeNode) -> None:
            if not root:
                return
            traversal(root.left)
            traversal(root.right)
            res.append(root.val)

        res = []
        traversal(root)
        return res


class Iter:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # root left right
        # 所以入栈的顺序是right left
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 中序遍历的迭代和前后序不同，因为先访问的是root
        # 而root需要在root.left后添加到答案
        # 所以访问节点需要借助指针 找到最左子节点
        stack = []
        res = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)  # 栈中顺序是中 左
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right  # 有右孩子下次循环就会把右压入栈
        return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]


class Unify:
    # 迭代统一写法 来源于中序遍历
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [], []
        cur = root
        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [], []
        cur = root
        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            cur = cur.left
        return res[::-1]


