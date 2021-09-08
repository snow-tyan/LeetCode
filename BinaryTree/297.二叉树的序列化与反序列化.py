'''
297.二叉树的序列化与反序列化

单单一个前序遍历是无法还原二叉树的，但是如果序列中包含空指针信息，就可以还原
'''
from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = deque()
        queue.append(root)
        seq = ''
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    seq += ',#'
                elif not seq:
                    seq += f'{node.val}'
                else:
                    seq += f',{node.val}'
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
        return seq

        # if not root:
        #     return '#'
        # return f'{root.val},{self.serialize(root.left)},{self.serialize(root.right)}'
        # return f'{self.serialize(root.left)},{self.serialize(root.right)},{root.val}'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        serial = data.split(',')  # return a list
        print(data)

        # def decodePreorder(serial: List) -> TreeNode:
        #     first = serial.pop(0)
        #     if first == '#':
        #         return None
        #     root = TreeNode(first)
        #     root.left = decodePreorder(serial)
        #     root.right = decodePreorder(serial)
        #     return root
        #
        # def decodePostorder(serial: List) -> TreeNode:
        #     last = serial.pop()
        #     if last == '#':
        #         return None
        #     root = TreeNode(last)
        #     # 先右后左
        #     root.right = decodePostorder(serial)
        #     root.left = decodePostorder(serial)
        #     return root
        #
        # # return decodePreorder(serial)
        # return decodePostorder(serial)

        if serial[0] == '':
            return None
        root = TreeNode(serial[0])
        queue = deque()
        queue.append(root)
        i = 0
        while i + 1 < len(serial):
            node = queue.popleft()
            # 每个非空节点后面必有俩孩子(孩子可能是空节点)
            # 通过i标识孩子位置
            left = serial[i + 1]
            i += 1
            if left != '#':
                node.left = TreeNode(left)
                queue.append(node.left)

            right = serial[i + 1]
            i += 1
            if right != '#':
                node.right = TreeNode(right)
                queue.append(node.right)

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

root = TreeNode(1)
a = TreeNode(2)
b = TreeNode(3)
c = TreeNode(4)
d = TreeNode(5)
root.left = a
root.right = b
b.left = c
b.right = d

ser = Codec()
der = Codec()
# print(ser.serialize(root))
der.deserialize(ser.serialize(None))
