'''
9.22 每日一题
725.分隔链表
'''
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        cnt = 0
        cur = head
        while cur:
            cnt += 1
            cur = cur.next
        quo, remain = cnt // k, cnt % k  # quo每个链表长度，remain余数

        res = []
        new_head = head
        j = 0
        while new_head:
            res.append(new_head)
            # 前remain个链表 长度quo+1
            length = quo if j < remain else quo - 1
            j += 1
            for i in range(length):
                new_head = new_head.next
            tmp = new_head.next
            new_head.next = None
            new_head = tmp
        while len(res) < k:
            res.append(None)  # 空指针
        return res
