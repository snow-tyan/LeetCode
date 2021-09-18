'''
332.重新安排行程 太难了
'''
from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def backtracking(from_point: str) -> bool:
            # 终止条件
            if len(path) == len(tickets) + 1:
                return True
            targets[from_point].sort()
            for _ in targets[from_point]:
                # 必须及时删除，避免出现死循环
                to_point = targets[from_point].pop(0)
                path.append(to_point)
                # 只要找到一个就可以返回了
                if backtracking(to_point):
                    return True
                path.pop()
                targets[from_point].append(to_point)
            return False

        # 记录航班映射关系
        targets = defaultdict(list)  # target={出发机场：{到达机场：航班次数}}
        # 初始化 (from,to)
        for f, t in tickets:
            targets[f].append(t)
        # print(targets)
        '''
        targets
         {'MUC': ['LHR'], 'JFK': ['MUC'], 'SFO': ['SJC'], 'LHR': ['SFO']}
        '''
        path = ["JFK"]
        backtracking("JFK")
        return path


solve = Solution()
print(solve.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
