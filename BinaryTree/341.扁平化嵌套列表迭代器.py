'''
341.打印嵌套列表
输入：[[1,1],2,[1,1]]
输出：[1,1,2,1,1]

输入：[1,[4,[6]]]
输出：[1,4,6]
'''

from typing import List


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.queue = []

        # N叉树的前序遍历
        def preorder(nestedList):
            for elem in nestedList:
                if elem.isInteger():
                    self.queue.append(elem)
                else:
                    preorder(elem.getList())

        preorder(nestedList)

    def next(self) -> int:
        if self.hasNext():
            return self.queue.pop(0)
        return -1

    def hasNext(self) -> bool:
        if self.queue:
            return True
        return False
