'''
每日一题 8.31
1109.航班预订统计
'''
from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # answer = [0] * n
        # for booking in bookings:
        #     start, end, val = booking[0], booking[1], booking[2]
        #     while start <= end:
        #         answer[start - 1] += val
        #         start += 1
        #
        # return answer

        inc = [0] * n
        for b in bookings:
            start, end, val = b
            inc[start - 1] += val
            if end < n:
                inc[end] -= val

        print(inc)
        # 前缀和
        for i in range(1, n):
            inc[i] += inc[i - 1]
        return inc


if __name__ == '__main__':
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    n = 5

    solve = Solution()
    print(solve.corpFlightBookings(bookings, n))

