'''
棋盘问题
51.N皇后
37.解数独
'''
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 各皇后不能同行、同列、同斜线 1<=n<=9
        def isvalid(row: int, col: int) -> bool:
            # 行不用检查，因为一层递归只会选for循环里一个元素
            # 剪枝：检查到当前行、列
            # 检查列
            for i in range(row):
                if path[i][col] == 'Q':
                    return False
            # 检查左上
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if path[i][j] == 'Q':
                    return False
            # 检查右上
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
                if path[i][j] == 'Q':
                    return False
            return True

        def backtracking(row: int) -> None:
            if row == n:
                temp = []
                for p in path:
                    temp.append(''.join(p))
                res.append(temp)
                return
            for col in range(n):  # for循环遍历一行，递归遍历一列
                if not isvalid(row, col):
                    continue
                path[row][col] = 'Q'  # 放置皇后
                backtracking(row + 1)  # 注意这里是下一行
                path[row][col] = '.'  # 回溯

        res = []
        path = [['.'] * n for _ in range(n)]
        backtracking(0)
        return res

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 每个位置都要放置数字 并检查是否合法
        def isvalid(row: int, col: int, val: str) -> bool:
            # 行
            for j in range(9):
                if board[row][j] == val:
                    return False
            # 列
            for i in range(9):
                if board[i][col] == val:
                    return False
            # 3*3 棋盘内是否合法
            inner_row = row // 3 * 3
            inner_col = col // 3 * 3
            for i in range(inner_row, inner_row + 3):
                for j in range(inner_col, inner_col + 3):
                    if board[i][j] == val:
                        return False
            return True

        def backtracking() -> bool:
            for i in range(m):  # 遍历行
                for j in range(n):  # 遍历列
                    if board[i][j] != '.':  # 是'.'才需要填
                        continue
                    for k in range(1, 10):  # k=1,2,3,...,9
                        if not isvalid(i, j, str(k)):  # [i][j]放入k是否合法
                            continue
                        board[i][j] = str(k)
                        if backtracking():
                            return True
                        board[i][j] = '.'
                    return False  # 1-9都不能放置，返回False
            return True

        m, n = len(board), len(board[0])
        print('-' * 10, 'before', '-' * 10)
        print(board)
        backtracking()
        print('-' * 10, 'after', '-' * 10)
        print(board)


solve = Solution()
# print(solve.solveNQueens(4))
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
solve.solveSudoku(board)
