'''
59.螺旋矩阵II
54.螺旋矩阵
'''
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        left, right, up, down = 0, n - 1, 0, n - 1
        number = 1
        while left < right and up < down:  # 一个while围一圈
            for i in range(left, right):  # -->
                res[up][i] = number
                number += 1

            for j in range(up, down):  # |
                res[j][right] = number  # |
                number += 1  # V

            for i in range(right, left, -1):  # <--
                res[down][i] = number
                number += 1

            for j in range(down, up, -1):  # ^
                res[j][left] = number  # |
                number += 1  # |

            left += 1
            right -= 1
            up += 1
            down -= 1

        if n % 2 != 0:  # 如果是奇数还要填中间的
            res[n // 2][n // 2] = number

        return res

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m, n = len(matrix), len(matrix[0])
        left, right, up, down = 0, n - 1, 0, m - 1
        while left < right and up < down:
            for i in range(left, right):
                res.append(matrix[up][i])
            for j in range(up, down):
                res.append(matrix[j][right])
            for i in range(right, left, -1):
                res.append(matrix[down][i])
            for j in range(down, up, -1):
                res.append(matrix[j][left])
            left += 1
            right -= 1
            up += 1
            down -= 1
        if left < right and up == down:
            for i in range(left, right + 1):
                res.append(matrix[up][i])
        if up < down and left == right:
            for j in range(up, down + 1):
                res.append(matrix[j][right])
        if m == n and n % 2 != 0:
            res.append(matrix[n // 2][n // 2])
        # print(left, right, up, down)
        return res


solve = Solution()
# print(solve.generateMatrix(3))
print(solve.spiralOrder([[1, 2, 3], [12, 13, 4], [11, 14, 5], [10, 15, 6], [9, 8, 7]]))
