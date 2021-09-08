'''
206.反转链表
92.反转链表II
25.K个一组反转链表 hard
234.回文链表
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 反转整个链表
    def reverseList(self, head: ListNode) -> ListNode:
        # # 指针操作
        # # 遍历链表，将当前节点的next指针指向前一个节点
        # # 此前需要储存下一个节点
        # pre = None
        # cur = head
        # while cur:
        #     post = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = post
        # return pre

        # 递归 不遍历
        if not head or not head.next:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last

    # 反转链表前N个节点
    # 递归时记录第N+1个节点
    post = None

    def reverseN(self, head: ListNode, n: int) -> ListNode:
        # 递归
        global post
        if n == 1:
            # 记录第N+1个节点
            post = head.next
            return head

        # 从下一个节点开始，递归反转前N-1个节点
        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        head.next = post

        return last

    # 反转链表中间某段
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 递归实现
        # left=1就是反转前N个节点问题, 否则就一直往后走
        if left == 1:
            return self.reverseN(head, right)
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head
