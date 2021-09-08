'''
207.课程表
210.课程表II

涉及知识点：dfs bfs 拓扑排序
'''
from typing import List, Tuple
import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 依赖问题，把问题转换成‘有向图’，判断图中有无环
        # 建图，以邻接表存储
        def buildGraph(numCourses: int, prerequisites: List[List[int]]) -> List[List[int]]:
            graph = []
            for i in range(numCourses):
                graph.append([])

            for side in prerequisites:
                a, b = side[1], side[0]  # 依赖关系b依赖a，就是a->b
                graph[a].append(b)

            return graph

        graph = buildGraph(numCourses, prerequisites)
        # print(graph)
        visited = [False] * numCourses  # 防止有环时走回头路
        has_cycle = False
        on_path = [False] * numCourses  # 记录dfs经过的路径

        # dfs graph邻接表，s某节点
        def dfs(graph: List[List[int]], s: int) -> None:
            nonlocal has_cycle
            if on_path[s]:
                has_cycle = True
            if visited[s] or has_cycle:
                return

            visited[s] = True
            on_path[s] = True  # 进入标记成True
            # 递归遍历节点s的所有边
            for node in graph[s]:
                dfs(graph, node)

            on_path[s] = False  # 离开标记成False

        # 并不是所有节点都相连，将所有节点都作为起点爆搜dfs
        for i in range(numCourses):
            dfs(graph, i)
        # print(visited)  # 全遍历了一次，应该都是True
        return not has_cycle

    # DFS建拓扑排序
    def findOrderDFS(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 依赖问题，把问题转换成‘有向图’，判断图中有无环
        # 建图，以邻接表存储
        def buildGraph(numCourses: int, prerequisites: List[List[int]]) -> List[List[int]]:
            graph = []
            for i in range(numCourses):
                graph.append([])

            for side in prerequisites:
                a, b = side[1], side[0]  # 依赖关系b依赖a，就是a->b
                graph[a].append(b)

            return graph

        res = []
        graph = buildGraph(numCourses, prerequisites)
        # print(graph)
        visited = [False] * numCourses  # 防止多次遍历
        has_cycle = False
        on_path = [False] * numCourses  # 记录dfs经过的路径

        # dfs graph邻接表，s某节点
        def dfs(graph: List[List[int]], s: int) -> None:
            nonlocal has_cycle
            if on_path[s]:
                has_cycle = True
            if visited[s] or has_cycle:
                return

            visited[s] = True
            on_path[s] = True  # 进入标记成True
            # 递归遍历节点s的所有边
            for node in graph[s]:
                dfs(graph, node)

            on_path[s] = False  # 离开标记成False
            res.append(s)  # 离开时将该节点加入答案

        # 并不是所有节点都相连，将所有节点都作为起点爆搜dfs
        for i in range(numCourses):
            dfs(graph, i)
        # print(visited)  # 全遍历了一次，应该都是True
        # 遍历完，如果有环，返回空数组
        if has_cycle:
            return []
        return res[::-1]

    # BFS建拓扑排序
    def findOrderBFS(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 建图，以邻接表存储
        def buildGraph(numCourses: int, prerequisites: List[List[int]]) -> Tuple[List[List[int]], List[int]]:
            graph = []  # 邻接表
            indeg = [0] * numCourses  # 入度表

            for i in range(numCourses):  # 直接[[]]*numCourses建表有问题
                graph.append([])
            for side in prerequisites:
                a, b = side[1], side[0]  # 依赖关系b依赖a，就是a->b
                graph[a].append(b)
                indeg[b] += 1

            return graph, indeg

        graph, indeg = buildGraph(numCourses, prerequisites)
        res = []
        # print(graph)
        # print(indeg)

        # 将所有入度为 0 的节点放入队列中
        queue = collections.deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                queue.append(i)

        while queue:
            # 队首节点出队，放入答案中
            node = queue.popleft()
            res.append(node)
            # 将该节点相邻节点入度-1
            for neighbor in graph[node]:
                indeg[neighbor] -= 1
                # 相邻节点入度为 0 则入队
                if indeg[neighbor] == 0:
                    queue.append(neighbor)

        if len(res) != numCourses:  # 如果拓扑排序没排完，则说明有环，返回空
            return []
        return res


def buildGraph(numCourses: int, prerequisites: List[List[int]]) -> Tuple[List[List[int]], List[int]]:
    graph = []  # 邻接表
    indeg = [0] * numCourses  # 每个节点的入度

    for i in range(numCourses):
        graph.append([])

    for side in prerequisites:
        a, b = side[1], side[0]  # 依赖关系b依赖a，就是a->b
        graph[a].append(b)
        indeg[b] += 1

    return graph, indeg


numCourses = 3
prerequisites = [[2, 1], [1, 0]]
graph, indeg = buildGraph(numCourses, prerequisites)
print(graph)
print(indeg)
