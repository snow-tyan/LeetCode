'''
21.合并两个有序链表
23.合并K个升序链表
141.环形链表
142.环形链表II
876.链表的中间节点
160.相交链表
19.删除链表的倒数第N个节点

链表常用技巧：
1 哑结点 dummy
2 双指针 快慢指针
'''
from typing import List
from queue import PriorityQueue  # queue库中队列，put()入队，get()出队
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    #
    # def __lt__(self, other):
    #     return self.val < other.val


class Solution:
    # 合并两个有序链表
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        # 一个链表已经遍历完
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # # 还能这样操作？
        # def __lt__(a: ListNode, b: ListNode):
        #     return a.val < b.val
        # ListNode.__lt__ = __lt__
        #
        # dummy = ListNode()
        # cur = dummy
        #
        # from queue import PriorityQueue
        # queue = PriorityQueue()
        # # 将k个链表的头结点加入优先级队列
        # for list in lists:
        #     if list:
        #         queue.put(list)  # 需重载__lt__()方法
        # while not queue.empty():
        #     node = queue.get()
        #     if node.next:
        #         queue.put(node.next)
        #     cur.next = node
        #     cur = cur.next
        # return dummy.next

        dummy = ListNode()
        cur = dummy
        heap = []  # 用heapq维护
        # 将k个链表的所有结点一次性加入优先级队列
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next

        while heap:
            val = heapq.heappop(heap)
            node = ListNode(val)
            cur.next = node
            cur = cur.next
        return dummy.next

    # 链表中间节点
    def middleNode(self, head: ListNode) -> ListNode:
        # 如果有两个中间结点，则返回第二个中间结点
        # 快慢指针，不用哑节点正好
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    # 判断是否链表有环
    def hasCycle(self, head: ListNode) -> bool:
        # 快慢指针
        # 若快指针与满指针相遇则有环
        if not head:
            return False
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    # 返回环形链表的入环节点
    def detectCycle(self, head: ListNode) -> ListNode:
        # 返回入环的第一个节点
        # 这是个数学题
        slow, fast = head, head
        has_cycle = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # 相遇
            if fast == slow:
                has_cycle = True
                break

        # 无环
        if not has_cycle:
            return None
        # 有环
        while head != fast:
            head = head.next
            fast = fast.next

        return head

    # 相交链表
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1, p2 = headA, headB
        # p1走A+B，p2走B+A。若走到头还没相遇，则双双等于NULL结束循环。
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA

        return p1

    # 删除倒数第n个节点
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 哑节点，省判断
        # head走n步，pre从哑结点出发再同步走
        # 当head走到null时，pre刚好走到要删除节点的前驱节点
        dummy = ListNode(next=head)
        pre = dummy
        for _ in range(n):
            head = head.next
        while head:
            head = head.next
            pre = pre.next
        pre.next = pre.next.next
        return dummy.next


if __name__ == '__main__':
    l1 = ListNode(1, next=(ListNode(4, next=(ListNode(5)))))
    l2 = ListNode(1, next=(ListNode(3, next=(ListNode(4)))))
    l3 = ListNode(2, next=(ListNode(6)))
    # lists = [[1,4,5],[1,3,4],[2,6]]
    lists = [l1, l2, l3]
    solve = Solution()
    solve.mergeKLists(lists)
