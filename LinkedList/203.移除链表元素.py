'''
链表
203.移除链表元素
24.两两交换链表中的节点
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(next=head)
        cur = head
        pre = dummy
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return dummy.next

    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # 链表至少两个节点
        dummy = ListNode(next=head)
        cur = dummy
        while cur.next and cur.next.next:
            one = cur.next  # 后一个
            two = one.next  # 后两个
            three = two.next  # 后三个
            cur.next = two
            cur.next.next = one
            cur.next.next.next = three

            cur = cur.next.next
        return dummy.next

