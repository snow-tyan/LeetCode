'''
344.反转字符串
541.反转字符串II
剑指offer05.替换空格
151.翻转字符串里的单词
557.反转字符串中的单词III
剑指offer58-II.左旋转字符串
'''
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    def reverseStr(self, s: str, k: int) -> str:
        def reverse(s: List[str]) -> List[str]:
            i, j = 0, len(s) - 1
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            return s

        res = list(s)
        for cur in range(0, len(s), 2 * k):
            res[cur:cur + k] = reverse(res[cur:cur + k])

        return ''.join(res)

    def replaceSpace(self, s: str) -> str:
        # return s.replace(' ', '%20')
        # 时间O(N) 空间O(N)
        res = []
        for ch in s:
            if ch == ' ':
                res.append('%20')
                continue
            res.append(ch)
        return ''.join(res)

        # 双指针 时间O(2N) 空间O(1)
        # 先遍历s统计空格个数，扩容到len(s)+2*space
        # i从后往前遍历，遇到空格添加'%20',j指向原s末尾,当ij相遇即结束

    def reverseWords(self, s: str) -> str:
        # 1 移除冗余空格
        # 2 翻转整个字符串
        # 3 翻转各单词
        def trim_spaces(s: str) -> List[str]:  # 移除多余空格
            n = len(s)
            i = 0
            j = n - 1
            while i <= j and s[i] == ' ':  # 开头的空格
                i += 1
            while i <= j and s[j] == ' ':  # 结尾的空格
                j = j - 1
            res = []
            while i <= j:  # 单词中间多余的空格
                if s[i] != ' ':
                    res.append(s[i])
                elif res[-1] != ' ':  # 当前位置是空格，但是相邻的上一个位置不是空格，则该空格是合理的
                    res.append(s[i])
                i += 1
            return res

        def reverse_string(s: List[str], i: int, j: int) -> None:
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        def reverse_word(s: List[str]) -> None:
            start = 0
            end = 0
            n = len(s)
            while start < n:
                while end < n and s[end] != ' ':
                    end += 1
                reverse_string(s, start, end - 1)
                start = end + 1
                end += 1

        s = trim_spaces(s)
        reverse_string(s, 0, len(s) - 1)
        reverse_word(s)
        return ''.join(s)

    def reverseWords3(self, s: str) -> str:
        def reverse_string(s: List[str], i: int, j: int) -> None:
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        n = len(s)
        s = list(s)
        start = 0
        end = 0
        while start < n:
            while end < n and s[end] != ' ':
                end += 1
            reverse_string(s, start, end - 1)  # 翻转一个单词
            start = end + 1
            end += 1

        return ''.join(s)

    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]
        # 若规定空间O(1)
        # 1 反转前n个字符串 2 反转n到末尾字符串 3 反转整个字符串

