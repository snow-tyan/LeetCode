'''
133.克隆图
返回无向图的深拷贝
'''

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        # {node: clone_node}
        # 不存node.neighbor信息
        self.cloned = {}  # 标记已克隆过的节点，防止重复克隆

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        if node in self.cloned:
            return self.cloned[node]

        clone_node = Node(val=node.val, neighbors=[])  # 克隆val并添加到哈希map中

        self.cloned[node] = clone_node

        # 递归克隆neighbors
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(neighbor) for neighbor in node.neighbors]
        return clone_node

