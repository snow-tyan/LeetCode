'''
134.加油站
781.森林中的兔子
179.最大数
611.有效三角形个数
'''
from typing import List
from collections import Counter
import functools


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 从说明可知 sum(gas)<=sum(cost)
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        diff = [gas[i] - cost[i] for i in range(n)]
        print(diff)
        preSum = [0]  # 求diff前缀和，前缀和最小处出发，可保证油箱始终大于0
        for i in range(n):
            preSum.append(preSum[i] + diff[i])
        print(preSum)
        return preSum.index(min(preSum))

    def numRabbits(self, answers: List[int]) -> int:
        # 每个兔子看到和自己同色的兔子
        # 回答相同的兔子归为同一组(同色)
        count = Counter(answers)
        # print(count)
        # 如果有x只兔子回答y，则至少有math.ceil(x//(y+1))种颜色，每种颜色y+1只兔子
        # 向上取整 (分子+分母-1)/分母
        return sum((x + y) // (y + 1) * (y + 1) for y, x in count.items())

    def largestNumber(self, nums: List[int]) -> str:
        # 比较字符串大小 比较拼接结果a+b b+a
        nums_str = []
        res = ''
        for num in nums:
            nums_str.append(str(num))
        # functools.cmp_to_key 将比较函数转换成关键字函数
        # 比较函数接受2个参数返回1 0 -1；关键字函数接受1个参数返回可以用作关键字排序的值
        nums_str.sort(key=functools.cmp_to_key(lambda a, b: int(a + b) - int(b + a)), reverse=True)
        if nums_str[0] == '0':
            return '0'
        for num_str in nums_str:
            res += num_str
        return res

    def triangleNumber(self, nums: List[int]) -> int:
        # 三角形三条边 任意两边和大于第三边
        # 暴力 O((N-2)!)
        # 如果先排序a<=b<=c，那么必有a+c>b b+c>a 只需保证a+b>c
        n = len(nums)
        nums.sort()
        res = 0
        # 枚举a
        for i in range(n):
            # 枚举b
            for j in range(i + 1, n):
                # 二分查找c的上界
                left, right, k = j + 1, n - 1, j  # k是c所在区间的上界
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] < nums[i] + nums[j]:
                        k = mid
                        left = mid + 1
                    else:
                        right = mid - 1
                res += k - j  # [j+1, k]
        return res


solve = Solution()
# gas = [1, 2, 3, 4, 5]
# cost = [3, 4, 5, 1, 2]
# gas = [5, 8, 2, 8]
# cost = [6, 5, 6, 6]
# solve.canCompleteCircuit(gas, cost)
# answers = [1, 1, 2]
# print(solve.numRabbits(answers))
nums = [3, 30, 34, 5, 9]
print(solve.largestNumber(nums))
