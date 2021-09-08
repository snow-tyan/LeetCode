'''
每日一题 9.2
剑指offer22 链表中倒数第k个节点
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # 常规思路：遍历两遍链表
        # 1 得到链表长度
        # 2 再遍历一次，找到倒数第k个节点

        # 双指针 一次遍历
        # 1 cur指针先跑k个节点
        # 2 pre cur 一起跑，当cur跑到NULL时，pre停留位置即倒数第k个
        pre, cur = head, head
        for i in range(k):
            cur = cur.next
        while cur:
            cur = cur.next
            pre = pre.next
        return pre
