'''
BST
230.BST中第k小的数
538.BST转累加树
669.修剪BST树
108.有序数组转BST树
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

    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return root
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root

    def trimBSTIter(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return root
        # 1 让root在[low, high]范围内
        while root and (root.val > high or root.val < low):
            if root.val > high:
                root = root.left
            else:
                root = root.right
        cur = root
        while cur:
            while cur.left and cur.left.val < low:  # 左孩子<low
                cur.left = cur.left.right
            cur = cur.left
        cur = root
        while cur:
            while cur.right and cur.right.val > high:  # 右孩子>high
                cur.right = cur.right.left
            cur = cur.right
        return root

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
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
