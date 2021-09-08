'''
230.BST中第k小的数
538.BST转累加树
1038.同538
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # # BST 中序遍历 就是有序的
        self.count = 0
        self.res = 0

        def inorder(root: TreeNode, k: int) -> None:
            if not root:
                return
            if self.count > k:
                return
            inorder(root.left, k)
            self.count += 1
            if self.count == k:
                self.res = root.val
            inorder(root.right, k)

        inorder(root, k)
        return self.res

    def convertBST(self, root: TreeNode) -> TreeNode:
        # # 常规思路
        # # 1 中序遍历 求和sum
        # # 2 再中序遍历 sum-=上个节点的值
        # def inorder(root: TreeNode) -> List[int]:
        #     if not root:
        #         return []
        #     res = []
        #     res.extend(inorder(root.left))
        #     res.append(root.val)
        #     res.extend(inorder(root.right))
        #     return res

        # self.total = sum(inorder(root))  # 即最左端节点的值
        # print(self.total)

        # def modify(root: TreeNode) -> TreeNode:
        #     if not root:
        #         return root
        #     modify(root.left)
        #     self.total -= root.val  # total减去当前节点
        #     root.val += self.total  # val加上当前节点的值，就相当于total减去上一个节点的值
        #     modify(root.right)
        #     return root

        # return modify(root)

        # 逆向中序遍历 right -> root -> left
        # 其结果也是个有序数组。遍历的时候即可进行累加操作
        self.sum = 0

        def reverseInorder(root: TreeNode) -> None:
            if not root:
                return
            reverseInorder(root.right)
            root.val += self.sum
            self.sum = root.val
            reverseInorder(root.left)

        reverseInorder(root)
        return root


if __name__ == '__main__':
    solve = Solution()
    root = TreeNode(5)
    a = TreeNode(3)
    b = TreeNode(2)
    c = TreeNode(1)
    d = TreeNode(4)
    e = TreeNode(6)
    root.left = a
    root.right = e
    a.left = b
    a.right = d
    b.left = c

    print(solve.kthSmallest(root, 3))
