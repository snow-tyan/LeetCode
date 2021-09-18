'''
切割问题
131.切割回文子串 难
93.复原IP地址 难
'''
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isvalid(s: str) -> bool:
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def backtracking(start_idx: int) -> None:
            if start_idx == len(s):
                res.append(path[:])
                return
            for i in range(start_idx, len(s)):  # i 宽度 同层切割位置
                substr = s[start_idx:i + 1]  # start_idx 深度 下层切割起始位置
                if not isvalid(substr):  # 前段不合法，还有继续遍历
                    continue
                path.append(substr)
                backtracking(i + 1)
                path.pop()

        res = []
        path = []
        backtracking(0)
        return res

    def restoreIpAddresses(self, s: str) -> List[str]:
        def isvalid(s: str) -> bool:
            if not s:
                return False
            if len(s) != 1 and s[0] == '0' or int(s) > 255:  # 前导0不合法，单0合法
                return False
            return True

        def backtracking(start_idx: int, point_num: int) -> None:
            if point_num == 3:  # 出口 已经有三个点 分成四段
                # 检查第四段
                final_str = s[start_idx:]
                if isvalid(final_str):
                    path.append(final_str)
                    res.append(''.join(path))
                    path.pop()
                return
            for i in range(start_idx, len(s)):  # i 宽度 同层切割位置
                substr = s[start_idx:i + 1]  # start_idx 深度 下层切割起始位置
                if not isvalid(substr):  # 前段不合法，不用走了
                    break
                path.append(substr + '.')
                point_num += 1
                backtracking(i + 1, point_num)
                path.pop()
                point_num -= 1

        res = []
        path = []
        backtracking(0, 0)
        return res


solve = Solution()
# print(solve.partition('aab'))
# print(solve.restoreIpAddresses('19216811'))