'''
BST
98.验证二叉搜索树是否合法
701.二叉搜索树的插入
450.二叉搜索树的删除 *
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_val = float('-inf')

    def isValidBST(self, root: TreeNode) -> bool:
        # 最简单的做法：中序遍历，存下结果 看是否为升序

        # 递归：每次只检查当前值是不是比上个节点的值大
        if not root:
            return True
        # 中序
        left = self.isValidBST(root.left)
        if self.max_val < root.val:
            self.max_val = root.val
        else:
            return False
        right = self.isValidBST(root.right)

        return left and right

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
        # 2 删除 五种情况
        #    1 没找到，遍历到空结点返回
        #    2 是叶子节点  返回NULL
        #    3 左孩子为空  返回右孩子
        #    4 右孩子为空  返回左孩子
        #    5 左右孩子均非空
        #        1 左子树接到右子树最左边
        #        2 或将右子树接到左子树最右边

        # ps.第五种情况通用的删除 是root与孩子节点值做交换然后删掉孩子节点
        def leftmost(root: TreeNode) -> TreeNode:
            # root必有左右孩子
            while root.left:
                root = root.left
            return root

        def rightmost(root: TreeNode) -> TreeNode:
            while root.right:
                root = root.right
            return root

        if not root:
            return root
        if root.val == key:  # 找到了
            # 2 叶子节点，直接删掉
            # 3 4 有一个孩子，孩子代替该节点
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # 5 左右都有孩子
            # 1 左子树接到右子树最左边
            # r_leftmost = leftmost(root.right)
            # r_leftmost.left = root.left
            # temp = root
            # root = root.right  # 返回右子树
            # del temp
            # return root

            # 2 右子树接到左子树最右边
            l_rightmost = rightmost(root.left)
            l_rightmost.right = root.right
            temp = root
            root = root.left
            del temp
            return root

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
