'''
707.设计链表
单链表： 头插O(1) 尾插O(N) 其他O(k) k为索引
双链表： 头插、尾插 O(1) 其他O(min(k, N-k))
'''


class ListNode1:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListNode:
    def __init__(self, val=0, pre=None, next=None):
        self.val = val
        self.pre = pre
        self.next = next


class MyLinkedList1:
    def __init__(self):
        self.size = 0
        self.dummy = ListNode1(0)  # dummy node

    def get(self, index: int) -> int:
        # 获取第index个节点的值，无效返回-1
        if index < 0 or index >= self.size:
            return -1

        pre = self.dummy
        for _ in range(index):
            pre = pre.next
        return pre.next.val

    def addAtHead(self, val: int) -> None:
        # 头插
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        # 尾插
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        # 在第index个节点前插入
        # index==0 头插 index=self.size 尾插
        # 有效 index [0, size-1]
        if index < 0 or index > self.size:
            return

        pre = self.dummy
        for _ in range(index):
            pre = pre.next
        node = ListNode1(val, next=pre.next)
        pre.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        # 若index有效，删除第index个节点
        if index < 0 or index >= self.size:
            return
        pre = self.dummy
        for _ in range(index):
            pre = pre.next

        pre.next = pre.next.next
        self.size -= 1


class MyLinkedList2:
    def __init__(self):
        self.size = 0
        self.dummy_head = ListNode()  # dummy head node
        self.dummy_tail = ListNode()  # dummy tail node
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.pre = self.dummy_head

    # 决定从头还是从尾查
    def _find_directions(self, index: int) -> ListNode:
        if index >= self.size // 2:
            # 从尾查
            node = self.dummy_tail
            for _ in range(self.size - index):
                node = node.pre
        else:
            # 从头查
            node = self.dummy_head
            for _ in range(index + 1):
                node = node.next
        return node

    def get(self, index: int) -> int:
        # 获取第index个节点的值，无效返回-1
        if index < 0 or index >= self.size:
            return -1
        return self._find_directions(index).val

    def addAtHead(self, val: int) -> None:
        # 头插
        self._insert(self.dummy_head, self.dummy_head.next, val)

    def addAtTail(self, val: int) -> None:
        # 尾插
        self._insert(self.dummy_tail.pre, self.dummy_tail, val)

    def addAtIndex(self, index: int, val: int) -> None:
        # 在第index个节点前插入
        # index==0 头插 index=self.size 尾插
        # 有效 index [0, size-1]
        if index < 0 or index > self.size:
            return
        node = self._find_directions(index)
        self._insert(node.pre, node, val)

    def _insert(self, pre: ListNode, next: ListNode, val: int) -> None:
        '''
        pre:  插入后的前一个节点
        next: 插入后的后一个节点
        '''
        node = ListNode(val)
        pre.next = node
        next.pre = node
        node.pre = pre
        node.next = next
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        # 若index有效，删除第index个节点
        if index < 0 or index >= self.size:
            return

        node = self._find_directions(index)
        node.pre.next = node.next
        node.next.pre = node.pre
        self.size -= 1


obj = MyLinkedList1()
param_1 = obj.get(1)
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1, 2)
obj.deleteAtIndex(2)
