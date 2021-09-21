'''
字符串匹配
KMP 有空再看
28.实现strStr()
459.重复的子字符串
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    def repeatedSubstringPattern(self, s: str) -> bool:
        # 若s有重复子串，则至少两次
        # s+s则至少四次，去除首位元素，即人为破坏两次，还剩至少两次
        # 若s无重复子串，则s+s破坏两次后不再含s
        return True if (s + s).find(s, 1, 2 * len(s) - 1) != -1 else False
