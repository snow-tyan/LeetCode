'''
每日一题 9.7
1221. 分割平衡字符串
'''


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        count = [0, 0]
        for i in range(len(s)):
            if s[i] == 'L':
                count[0] += 1
            else:
                count[1] += 1
            if count[0] == count[1]:
                res += 1

        return res


s = "RLLLLRRRLR"
solve = Solution()
print(solve.balancedStringSplit(s))
