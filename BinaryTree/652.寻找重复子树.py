from typing import List, Optional
from collections import Counter


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # 序列化二叉树，将所有子树存入map中
        # 重复子树，只需返回一次
        count = Counter()  # 字典子类，计数
        res = []

        def collect(node: TreeNode) -> str:
            if not node:
                return '#'

            serial = f'{node.val},{collect(node.left)},{collect(node.right)}'
            count[serial] += 1  # 当值不存在时，为0  update方法也不是覆盖而是加1
            # 加且仅加一次
            if count[serial] == 2:
                res.append(node)
            return serial

        collect(root)
        return res


if __name__ == '__main__':
    root = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(3)
    c = TreeNode(4)
    d = TreeNode(2)
    e = TreeNode(4)
    f = TreeNode(4)

    root.left, root.right = a, b
    a.left = c
    b.left, b.right = d, e
    d.left = f

    solve = Solution()
    print(solve.findDuplicateSubtrees(root))

