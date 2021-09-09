'''
139.单词拆分
DFS+BFS+DP
'''
from typing import List


class Solution:
    # DFS -- TLE
    def wordBreakDFS(self, s: str, wordDict: List[str]) -> bool:
        # dfs 遍历s，每次检查
        # 1 s[:i]是否在字典中
        # 2 s[i:]是否可以break
        if not s:
            return True
        for i in range(len(s)):
            if s[:i + 1] in wordDict and \
                    self.wordBreakDFS(s[i + 1:], wordDict):
                return True

        return False

    # DFS + memo
    def __init__(self):
        self.memo = {}

    def wordBreakDFSMEMO(self, s: str, wordDict: List[str]) -> bool:
        # dfs 遍历s，每次检查
        # 1 s[:i]是否在字典中
        # 2 s[i:]是否可以break
        if not s:
            return True
        if s in self.memo.keys():
            return self.memo[s]
        for i in range(len(s)):
            if s[:i + 1] in wordDict and \
                    self.wordBreakDFSMEMO(s[i + 1:], wordDict):
                self.memo[s[i + 1:]] = True
                return True
        self.memo[s] = False
        return False

    # BFS -- TLE
    def wordBreakBFS(self, s: str, wordDict: List[str]) -> bool:
        # 维护一个队列
        # 遍历字符串，当其前缀在单词表中，子串入队
        # 直到其子串为空，返回True
        queue = [s]
        while queue:
            string = queue.pop(0)
            # 遍历
            for i in range(len(string)):
                if string[:i + 1] in wordDict:
                    if string[i + 1:] == '':
                        return True
                    queue.append(string[i + 1:])  # 这里不能提前结束，还要接着遍历
        return False

    # BFS + visited
    def wordBreakBFSVISITED(self, s: str, wordDict: List[str]) -> bool:
        # 遍历字符串，当其前缀在单词表中，子串入队
        # 直到其子串为空，返回True
        # visited数组记录访问过的节点
        visited = []
        queue = [s]
        while queue:
            string = queue.pop(0)
            if string in visited:
                continue
            visited.append(string)
            # 遍历
            for i in range(len(string)):
                if string[:i + 1] in wordDict:
                    if string[i + 1:] == '':
                        return True
                    queue.append(string[i + 1:])  # 这里不能提前结束，还要接着遍历
        return False

    # DP
    def wordBreakDP(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] s[:i]能否break
        # 取决于：
        # 1 其前缀子串s[:j]是否为True -> dp[j] (j遍历指针,0<=j<=i)
        # 2 剩余子串s[j:i]是否在单词表中
        n = len(s)
        dp = [False] * (n + 1)
        # base case
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i - 1, -1, -1):
                if dp[i]:
                    break
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[n]


solve = Solution()
# s = "catsand"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
# print(solve.wordBreakDFS(s, wordDict))
# print(solve.wordBreakDFSMEMO(s, wordDict))
# print(solve.wordBreakBFS(s, wordDict))
# print(solve.wordBreakBFSVISITED(s, wordDict))
print(solve.wordBreakDP(s, wordDict))
