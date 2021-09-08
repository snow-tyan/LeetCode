from typing import List
from collections import deque
# 涉及题型
# 递归、非递归、~莫里斯遍历~、N叉树前后序遍历
'''
144.二叉树的前序遍历
94.二叉树的中序遍历
145.二叉树的后序遍历
102.二叉树的层序遍历
103.二叉树的锯齿形层序遍历
589.N叉树的前序遍历
590.N叉树的后序遍历
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# N叉树节点
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# 递归
class SolutionRecursion:
    # 前序遍历 root->left->right
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        result.append(root.val)
        result.extend(self.preorderTraversal(root.left))
        result.extend(self.preorderTraversal(root.right))
        return result

    # 中序遍历 left->root->right
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        result.extend(self.inorderTraversal(root.left))
        result.append(root.val)
        result.extend(self.inorderTraversal(root.right))
        return result

    # 后序遍历 left->right->root
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        result.extend(self.postorderTraversal(root.left))
        result.extend(self.postorderTraversal(root.right))
        result.append(root.val)
        return result


# 迭代
class SolutionIteration:
    # 前序遍历 root->left->right
    # DFS
    def preorderIter1(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    def preorderIter2(self, root: TreeNode) -> List[int]:
        result, stack = [], []
        cur = root
        while cur or stack:
            while cur:
                result.append(cur.val)
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        return result

    # 中序遍历 left->root->right
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 先用指针找到每棵子树最左下角，然后出栈
        result, stack = [], []
        cur = root
        while cur or stack:
            # 入栈  先入root 后入left
            while cur:
                stack.append(cur)
                cur = cur.left
            # 出栈
            cur = stack.pop()
            result.append(cur.val)

            cur = cur.right
        return result

    # 后序遍历 left->right->root
    # 即将前序 root->right->left 倒置
    def postorderIter1(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]

    def postorderIter2(self, root: TreeNode) -> List[int]:
        result, stack = [], []
        cur = root
        while cur or stack:
            while cur:
                result.append(cur.val)
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            cur = cur.left
        return result[::-1]

    def levelTraversal(self, root: TreeNode) -> List[List[int]]:
        # BFS
        # if not root:
        #     return []

        # cur_lay = [root]
        # result = []
        # while cur_lay:
        #     # 一层
        #     next_lay = []  # 存储下一层迭代信息 额外的空间开销
        #     cur_node = []  # 存储当前层节点
        #     for node in cur_lay:
        #         # 一个节点
        #         cur_node.append(node.val)
        #         if node.left:
        #             next_lay.append(node.left)
        #         if node.right:
        #             next_lay.append(node.right)
        #     result.append(cur_node)
        #     cur_lay = next_lay
        # return result

        if not root:
            return []

        queue = deque([root])
        result = []
        while queue:
            lay = []
            for _ in range(len(queue)):
                node = queue.popleft()
                lay.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(lay)
        return result

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        result = []
        cur_lay = [root]
        cnt = 1
        # 层
        while cur_lay:
            next_lay, cur_node = [], []
            # 节点
            for node in cur_lay:
                cur_node.append(node.val)
                if node.left:
                    next_lay.append(node.left)
                if node.right:
                    next_lay.append(node.right)

            if cnt % 2 == 0:
                cur_node = cur_node[::-1]

            result.append(cur_node)
            cnt += 1
            cur_lay = next_lay

        return result


class SolutionNTree:
    # 递归
    def preorderRecur(self, root: Node) -> List[int]:
        if not root:
            return []
        result = [root.val]
        if root.children:
            for node in root.children:
                result.extend(self.preorderRecur(node))

        return result

    # 迭代
    def preorderIter(self, root: Node) -> List[int]:
        if not root:
            return []

        stack = [root]
        result = []
        while stack:
            # 出栈，保存
            node = stack.pop()
            result.append(node.val)
            # 入栈
            if node.children:
                stack.extend(node.children[::-1])
        return result

    # 递归
    def postorderRecur(self, root: Node) -> List[int]:
        if not root:
            return []
        result = []
        if root.children:
            for node in root.children:
                result.extend(self.postorderRecur(node))
        result.append(root.val)
        return result

    # 迭代
    def postorderIter(self, root: Node) -> List[int]:
        if not root:
            return []

        stack = [root]
        result = []
        while stack:
            # 出栈，保存
            node = stack.pop()
            result.append(node.val)
            # 入栈
            if node.children:
                stack.extend(node.children)
        return result[::-1]


if __name__ == '__main__':
    '''
            2
          /   \
         0     4
          \   / \
           1 3   5
                  \
                   6 
    '''
    # 前序 [2, 0, 1, 4, 3, 5, 6]
    # 中序 [0, 1, 2, 3, 4, 5, 6]
    # 后序 [1, 0, 3, 6, 5, 4, 2]
    # 层序 [2, 0, 4, 1, 3, 5, 6]
    root = TreeNode(2)
    a = TreeNode(0)
    b = TreeNode(4)
    c = TreeNode(1)
    d = TreeNode(3)
    e = TreeNode(5)
    f = TreeNode(6)
    root.left = a
    root.right = b
    a.right = c
    b.left = d
    b.right = e
    e.right = f

    recur = SolutionRecursion()
    print(recur.preorderTraversal(root))
    print(recur.inorderTraversal(root))
    print(recur.postorderTraversal(root))

    iter = SolutionIteration()
    print(iter.preorderIter1(root))
    print(iter.preorderIter2(root))
    print(iter.inorderTraversal(root))
    print(iter.postorderIter1(root))
    print(iter.postorderIter2(root))
    print(iter.levelTraversal(root))

    '''N叉树
         1
       / | \
      3  2  4
     / \
    5   6
    '''
    root = Node(1)
    A = Node(3)
    B = Node(2)
    C = Node(4)
    D = Node(5)
    E = Node(6)
    root.children = A, B, C
    A.children = D, E

    NTree = SolutionNTree()
    print(NTree.preorderRecur(root))
    print(NTree.preorderIter(root))
    print(NTree.postorderRecur(root))
    print(NTree.postorderIter(root))
