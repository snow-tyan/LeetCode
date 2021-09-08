from typing import List

'''
96.不同的二叉搜索树 递归超时 -> 动规
95.不同的二叉搜索树II
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def numTrees(self, n: int) -> int:
        # 1 <= n <= 19
        nums = [0] * (n + 1)  # 0到n
        nums[0], nums[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(i):
                nums[i] += nums[j] * nums[i - j - 1]
        return nums[n]

    def generateTrees(self, n: int) -> List[TreeNode]:
        # 1 <= n <= 8
        def buildBST(low, high) -> List[TreeNode]:
            # low <= high
            res = []
            if low > high:
                res.append(None)
                return res

            mid = low
            while mid <= high:
                # List[TreeNode]
                left = buildBST(low, mid - 1)
                right = buildBST(mid + 1, high)
                for l in left:
                    for r in right:
                        root = TreeNode(mid)
                        root.left = l
                        root.right = r
                        res.append(root)
                mid += 1

            return res

        return buildBST(1, n)


if __name__ == '__main__':
    solve = Solution()
    print(solve.numTrees(8))
