'''
层序遍历
102.二叉树的层序遍历
107.二叉树的层序遍历II
199.二叉树的右视图
637.二叉树的层平均值
515.在每个树行中找最大值
116.填充每个节点的下一个右侧节点指针
117.填充每个节点的下一个右侧节点指针II
'''
from typing import List, Optional
import collections


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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = collections.deque([root])
        while queue:
            lay = []
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                lay.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(lay)
        return res

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([root])
        res = []
        while queue:
            lay = []
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                lay.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(lay)
        return res[::-1]

    def rightSideView(self, root: TreeNode) -> List[int]:
        # 右视图非右子节点 用栈不行
        # 层序遍历
        if not root:
            return []
        res = []
        queue = collections.deque([root])
        while queue:
            lay = []
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                lay.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(lay[-1])
        return res

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        res = []
        queue = collections.deque([root])
        while queue:
            sum = 0
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(sum / n)
        return res

    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        queue = collections.deque([root])
        while queue:
            # heap = []
            max_val = float('-inf')
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                # heapq.heappush(heap, -node.val)  # 大顶推
                max_val = max(max_val, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # res.append(-heapq.heappop(heap))
            res.append(max_val)
        return res

    # 递归解法
    def connectRecur(self, root: 'Node') -> 'Node':
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

    # 层次遍历
    def connectQueue(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = collections.deque([root])
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                node.next = queue[0] if i < n - 1 else None

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root

    # O(1)空间模拟
    def connect116(self, root: 'Node') -> 'Node':
        # 递归使用了栈空间，层次遍历使用了队列O(N)
        # 在当前层建立下一层的next，然后下一层顺着next遍历 可实现O(1)空间复杂度
        if not root:
            return root
        node = root
        while node.left:
            # 遍历该层节点，建立下层next
            cur = node
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next

            node = node.left  # 进入下层最左节点
        return root
