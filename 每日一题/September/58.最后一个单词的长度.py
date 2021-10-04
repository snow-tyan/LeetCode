'''
9.21 每日一题
58.最后一个单词的长度
'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt = 0
        i = len(s) - 1
        while s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            i -= 1
            cnt += 1

        return cnt
