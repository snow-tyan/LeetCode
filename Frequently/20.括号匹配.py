'''
括号匹配
20.有效括号
921.使括号有效的最小插入
1541.平衡括号串的最少插入
'''


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

    def minAddToMakeValid(self, s: str) -> int:
        # 右括号可以遍历完字符串再添加，但左括号必须添加在右括号前
        left, res = 0, 0
        for ch in s:
            if ch == '(':
                left += 1
            else:
                if left != 0:
                    left -= 1
                else:
                    res += 1
        res += left  # 加上需要添加的右括号数
        return res

    def minInsertions(self, s: str) -> int:
        # 右括号可以遍历完字符串再添加，但左括号必须添加在右括号前
        # 左括号必须匹配两个连续右括号
        # 维护左括号个数
        left, res = 0, 0
        i = 0
        n = len(s)
        while i < n:
            if s[i] == '(':
                left += 1
                i += 1
            else:
                if left > 0:
                    left -= 1
                else:
                    res += 1
                if i + 1 < n and s[i + 1] == ')':  # 如果连续的两个右括号
                    i += 2
                else:  # 如果是左括号或字符串为空了
                    res += 1
                    i += 1

        res += left * 2
        return res
