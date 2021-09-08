'''
BST
100.判断俩二叉树是否相同
98.验证二叉搜索树是否合法
450.二叉搜索树的删除 *
700.二叉搜索树的查找
701.二叉搜索树的插入
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 两树均空
        if not p and not q:
            return True
        # 一空一非空
        elif not p or not q:
            return False

        res = False
        # 两树均非空，递归判断
        if p.val == q.val:
            # 左子树
            res = self.isSameTree(p.left, q.left)
            # 左子树真，才判断右子树
            if res:
                res = self.isSameTree(p.right, q.right)

        return res

    def isValidBST(self, root: TreeNode) -> bool:
        # 辅助函数，帮助递归，
        # root：节点 lower 下界 upper 上界
        def helper(root: TreeNode, lower=None, upper=None) -> bool:
            if not root:
                return True

            if lower and root.val <= lower.val:
                return False
            if upper and root.val >= upper.val:
                return False
            # 递归调用左子树，修改上界
            # 递归调用右子树，修改下界
            return helper(root.left, lower, root) and helper(root.right, root, upper)

        return helper(root)

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # 二叉搜索树
        # 返回该节点为root的子树
        if not root:
            return root

        if root.val == val:
            return root
        # val 大于 root， 则在左子树
        elif root.val > val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # 输入数据保证，val不同于原始二叉搜索树
        # 答案不唯一，返回任意有效结果
        # root为空，返回该节点
        if not root:
            return TreeNode(val)

        # 插入值小于root，插入到左子树
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        elif root.val < val:
            root.right = self.insertIntoBST(root.right, val)

        return root

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # 1 查找
        # 2 删除
        def getMinNode(root: TreeNode) -> TreeNode:
            # 已知root必有左右孩子
            # 二叉搜索树，最左端就是最小节点
            while root.left:
                root = root.left
            return root

        def getMaxNode(root: TreeNode) -> TreeNode:
            while root.right:
                root = root.right
            return root

        if not root:
            return root
        if root.val == key:
            # delete key
            # 如果是叶子节点，直接删掉
            # 如果有一个孩子，孩子代替该节点
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # 如果左右都有孩子，需要找到左子树最大节点或右子树最小节点代替
            # minNode = getMinNode(root.right)
            # root.val = minNode.val
            # root.right = self.deleteNode(root.right, minNode.val)

            maxNode = getMaxNode(root.left)
            root.val = maxNode.val
            root.left = self.deleteNode(root.left, maxNode.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        return root


if __name__ == '__main__':
    rootp = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(3)
    rootp.left = a
    rootp.right = b

    rootq = TreeNode(1)
    c = TreeNode(2)
    d = TreeNode(3)
    rootq.left = c
    rootq.right = d

    rootbst = TreeNode(2)
    e = TreeNode(1)
    f = TreeNode(3)
    rootbst.left = e
    rootbst.right = f

    root = TreeNode(5)
    a = TreeNode(3)
    b = TreeNode(6)
    c = TreeNode(2)
    d = TreeNode(4)
    e = TreeNode(7)
    root.left = a
    root.right = b
    a.left = c
    a.right = d
    b.right = e

    solve = Solution()
    print(solve.isSameTree(rootp, rootq))
    print(solve.isValidBST(rootq))
    print(solve.deleteNode(root, key=3))
