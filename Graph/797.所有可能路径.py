'''
图
797.所有可能路径

图的存储方式：邻接表、邻接矩阵
'''
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # 无环图
        res = []

        def dfs(graph: List[List[int]], s: int, path: List[int]) -> None:
            '''
            第s个节点：从0到n-1
            '''
            path.append(s)
            # 走到终点
            if s == len(graph) - 1:
                res.append(path.copy())
                path.pop()
                return

            for v in graph[s]:
                dfs(graph, v, path)

            path.pop()

        path = []
        dfs(graph, 0, path)
        return res


if __name__ == '__main__':
    graph = [[1, 2], [3], [3], []]
    solve = Solution()
    print(solve.allPathsSourceTarget(graph))
