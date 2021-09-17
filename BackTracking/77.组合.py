'''
组合问题
77.组合
216.组合总和III
17.电话号码的字母组合
39.组合总和
40.组合总和II 难
'''
from typing import List


class Solution:
    # 返回 1...n 所有可能k个数的组合
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 两个全局变量
        res = []
        path = []  # 一次可能的结果

        # 组合问题不考虑顺序，因此需要start_index缩小范围
        def backtraking(start_idx: int) -> None:
            if len(path) == k:  # 出口
                res.append(path[:])
                return

            for i in range(start_idx, n + 1):
                # 剪枝：如果path+剩余区间已不足k则不需再遍历了
                if len(path) + n + 1 - i < k:
                    continue
                path.append(i)
                backtraking(i + 1)
                path.pop()

        backtraking(1)
        return res

    # 返回 相加之和为n 的k个正整数1...9组合
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []

        def backtracking(cur_sum: int, start_idx: int) -> None:
            if cur_sum > n:  # 剪枝
                return

            if len(path) == k:
                if cur_sum == n:
                    res.append(path[:])
                return

            for i in range(start_idx, 10):
                if len(path) + 10 - start_idx < k:  # 剪枝 剩余长度不足k
                    continue
                cur_sum += i
                path.append(i)
                backtracking(cur_sum, i + 1)
                cur_sum -= i
                path.pop()

        backtracking(0, 1)
        return res

    # 多个集合求组合
    def letterCombinations(self, digits: str) -> List[str]:
        mp = {0: '', 1: '', 2: 'abc', 3: 'def', 4: 'ghi',
              5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        res = []
        path = []

        def backtracking(index: int):
            if index == len(digits):  # 深度
                res.append(''.join(path))
                return
            # digit = ord(digits[index]) - ord('0')
            digit = int(digits[index])  # index遍历digits，也是递归深度
            for letter in mp[digit]:  # 宽度
                path.append(letter)
                backtracking(index + 1)
                path.pop()

        backtracking(0)
        return res

    # 从candidates中找出所有元素和为target的组合
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 可重复利用，组合个数无限制
        def backtracking(cur_sum: int, start_idx: int):
            if cur_sum > target:
                return
            if cur_sum == target:
                res.append(path[:])
                return
            for i in range(start_idx, len(candidates)):
                cur_sum += candidates[i]
                path.append(candidates[i])
                backtracking(cur_sum, i)
                path.pop()
                cur_sum -= candidates[i]

        res = []
        path = []
        backtracking(0, 0)
        return res

    # 从candidates中找出所有元素和为target的组合
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 每个数字在每个组合仅出现一次
        # 同一树层上相同数字只能使用一次；同一树枝上数字可以相同
        # 树层去重需要排序
        def backtracking(cur_sum: int, start_idx: int):
            if cur_sum > target:
                return
            if cur_sum == target:
                res.append(path[:])
                return
            for i in range(start_idx, n):
                # candidates[i] == candidates[i-1] 去重
                # 加上i>start_idx保证了，当前层会进continue 不会重复；但下一层不会进，可重复
                if i > start_idx and candidates[i] == candidates[i - 1]:
                    continue
                cur_sum += candidates[i]
                path.append(candidates[i])
                backtracking(cur_sum, i + 1)
                path.pop()
                cur_sum -= candidates[i]

        res = []
        path = []
        n = len(candidates)
        candidates.sort()  # 排序
        backtracking(0, 0)
        return res


solve = Solution()
# print(solve.combine(4, 4))
# print(solve.combinationSum3(9, 45))
# print(solve.letterCombinations('23'))
# print(solve.combinationSum(candidates=[2, 3, 6, 7], target=7))
# print(solve.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
