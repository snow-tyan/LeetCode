'''
回溯法 -> 抽象成N叉树结构 (集合大小->树宽度，递归深度->树深度)
1 组合问题 N个数按一定规则找出k个数的集合
2 切割问题 一个字符串按一定规则有几种切割方式
3 子集问题 一个N个数集合有多少符合条件的子集
4 排列问题 N个数按一定规则全排列，有几种排列方式
5 棋盘问题 N皇后，解数独

void backtracking(参数) {
    if (终⽌条件) {
        存放结果;
        return;
    }
    for (选择：本层集合中元素（树中节点孩⼦的数量就是集合的⼤⼩）) {
        处理节点;
        backtracking(路径，选择列表); // 递归
        回溯，撤销处理结果
    }
}

22.括号生成
46.全排列
'''
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n个左括号 n个右括号
        res = []

        def backtrack(strs: List[str], left: int, right: int) -> None:
            if len(strs) == 2 * n:
                res.append(''.join(strs))
                return
            if left < n:
                strs.append('(')
                backtrack(strs, left + 1, right)  # 递归生成括号
                strs.pop()  # 恢复现场
            if right < left:
                strs.append(')')
                backtrack(strs, left, right + 1)
                strs.pop()

        backtrack([], 0, 0)
        return res

    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking() -> None:
            if len(array) == n:
                res.append(array[:])  # 复制列表 array.copy()
                return
            for i in range(n):
                if visited[i]:
                    continue
                visited[i] = True
                array.append(nums[i])
                backtracking()
                array.pop()
                visited[i] = False

        res = []
        n = len(nums)
        array = []
        visited = [False] * n
        backtracking()
        return res


solve = Solution()
# print(solve.generateParenthesis(2))
nums = [1, 2, 3]
print(solve.permute(nums))
