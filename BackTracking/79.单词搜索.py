'''
79.单词搜索
212.单词搜索II
'''
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        # check(i, j, k) 检查board[i][j]是否能搜索到word[k:]
        def check(i: int, j: int, k: int) -> bool:
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            res = False
            visited.add((i, j))
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            res = True
                            break

            visited.remove((i, j))
            return res

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if check(i, j, 0):
                    return True
        return False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 暴力回溯 TLE
        res = []
        for word in words:
            if self.exist(board, word):
                res.append(word)
        return res


solve = Solution()
board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
word = 'eat'
words = ["oath", "pea", "eat", "rain"]
print(solve.exist(board, word))
print(solve.findWords(board, words))
