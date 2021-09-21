'''
232.用栈实现队列
225.用队列实现栈
20.有效的括号
1047.删除字符串中所有相邻重复项
150.逆波兰表达式求值
'''
from typing import List
import collections


class MyQueue:
    def __init__(self):
        # 进队：进stack1 出队：stack1->stack2再pop
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                x = self.stack1.pop()
                self.stack2.append(x)
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                x = self.stack1.pop()
                self.stack2.append(x)
        return self.stack2[-1]  # stack2.top()

    def empty(self) -> bool:
        return False if self.stack1 or self.stack2 else True


class MyStack:
    def __init__(self):
        # 和用栈实现队列思路不同
        # 队列2是用来备份队列1除了尾元素外的元素
        # 之所以不用list是list的pop(0)复杂度是O(N)
        self.que1 = collections.deque()
        self.que2 = collections.deque()

    def push(self, x: int) -> None:
        self.que1.append(x)

    def pop(self) -> int:
        while len(self.que1) > 1:
            x = self.que1.popleft()
            self.que2.append(x)
        y = self.que1.popleft()
        while self.que2:
            x = self.que2.popleft()
            self.que1.append(x)
        return y

    def top(self) -> int:
        while len(self.que1) > 1:
            x = self.que1.popleft()
            self.que2.append(x)
        y = self.que1.popleft()
        self.que2.append(y)
        while self.que2:
            x = self.que2.popleft()
            self.que1.append(x)
        return y

    def empty(self) -> bool:
        return False if self.que1 else True


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in '([{':  # 左括号入栈
                stack.append(ch)
            elif ch in ')]}':  # 右括号弹栈
                ch2 = stack.pop()
                # 看看是否匹配 不匹配直接False
                if ch == ')' and ch2 != '(' or ch == '[' and ch2 != ']' \
                        or ch == '{' and ch2 != '}':
                    return False

        if not stack:
            return True
        return False

    def removeDuplicates(self, s: str) -> str:
        # 栈
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
                continue
            stack.append(ch)
        return ''.join(stack)

    # 逆波兰表达式(RPN) 即后缀表达式
    def evalRPN(self, tokens: List[str]) -> int:
        def calc(t: str) -> str:
            b = int(stack.pop())
            a = int(stack.pop())
            c = 0
            if t == '+':
                c = a + b
            elif t == '-':
                c = a - b
            elif t == '*':
                c = a * b
            elif t == '/':
                # if a ^ b < 0:  # 异号
                #     c = -(abs(a) // abs(b))
                # else:
                #     c = a // b
                c = int(a / b)  # python a//b向下取整 负数情况不一致
            return str(c)

        stack = []
        for t in tokens:
            if t in '+-*/':
                stack.append(calc(t))
                continue
            stack.append(t)
        return int(stack[-1])


solve = Solution()
print(solve.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
