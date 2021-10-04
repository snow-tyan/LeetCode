'''
9.24 每日一题
430.扁平化多级双向链表
'''


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        # dummy = Node()
        # dummy.next = head
        # while head:
        #     if head.child:  # 如果当前节点有孩子，就把孩子接到当前节点后
        #         temp = head.next
        #         child = self.flatten(head.child)
        #         head.next = child
        #         child.prev = head
        #         head.child = None  # 孩子置空
        #         # head已经接上child，遍历head找最后一个节点
        #         while head.next:
        #             head = head.next
        #         head.next = temp
        #         if temp:
        #             temp.prev = head
        #     head = head.next
        # return dummy.next

        # 上述递归低效的原因是flatten返回的是孩子的头结点，而寻找孩子的尾结点又要遍历一遍孩子链表
        # 不如重写一个flatten函数返回孩子的尾结点
        def flatten_last(head: 'Node') -> 'Node':
            last = head
            while head:
                if head.child:
                    temp = head.next
                    child_last = flatten_last(head.child)
                    head.next = head.child
                    head.child.prev = head
                    head.child = None
                    if child_last:
                        child_last.next = temp
                    if temp:
                        temp.prev = child_last
                    head = child_last  # head指向child last
                last = head
                head = head.next
            return last

        dummy = Node()
        dummy.next = head
        flatten_last(head)
        return dummy.next
