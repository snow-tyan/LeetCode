'''
单调栈
739.每日温度
496.下一个更大元素
503.下一个更大元素II
42.接雨水
84.柱状图最大的矩形
85.最大矩形
402.移除k位数字
'''
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # # 暴力 O(n^2)
        # n = len(temperatures)
        # res = []
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if temperatures[j] > temperatures[i]:  # 搜索比i大的最近位置
        #             res.append(j - i)
        #             break
        #         elif j == n - 1:  # 搜到最后一个还搜不到 补0
        #             res.append(0)
        # res.append(0)  # 最后位置再补个0
        # return res

        # 单调栈 顺序指 从栈顶到栈底
        # 递增栈
        n = len(temperatures)
        stack = [0]
        res = [0] * n
        for i in range(1, n):
            # 若该元素小于等于栈顶元素，只管入栈
            # 如果该元素大于栈顶元素，栈内不能保持单调递增
            while stack and temperatures[i] > temperatures[stack[-1]]:
                top = stack.pop()
                res[top] = i - top
            stack.append(i)
        return res

    # nums1是nums2的子集，在nums2中搜索nums1的下一个最大元素
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # # 暴力 O(n^2)简单写一下
        # m, n = len(nums1), len(nums2)
        # res = []
        # flag = False
        # for i in range(m):
        #     for j in range(n):
        #         if nums2[j] == nums1[i]:  # 先找到nums1[i]在nums2中的位置，再去找下一个比其大的值
        #             flag = True
        #         if flag and nums2[j] > nums1[i]:
        #             res.append(nums2[j])
        #             flag = False
        #             break
        #         elif j == n - 1:  # 找不到就填-1
        #             res.append(-1)
        #             flag = False
        # return res

        # 单调栈 O(m+n)
        # 寻找nums2中每个元素的下一个最大元素，如果该元素在nums1中出现，那么添加到答案
        m, n = len(nums1), len(nums2)
        res = [-1] * m
        stack = [0]
        # 需要定义一个字典，用于查询nums1对应的下标 (存放结果)
        mp = {k: v for v, k in enumerate(nums1)}  # O(m)
        for i in range(n):  # O(n)
            while stack and nums2[i] > nums2[stack[-1]]:
                top = stack.pop()
                if nums2[top] in mp.keys():
                    index = mp[nums2[top]]
                    res[index] = nums2[i]
            stack.append(i)
        return res

    # 循环数组nums
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 单调栈
        # 循环数组，循环2n次 对n取余即可
        n = len(nums)
        res = [-1] * n
        stack = [0]
        for i in range(2 * n - 1):
            while stack and nums[i % n] > nums[stack[-1]]:
                top = stack.pop()
                res[top] = nums[i % n]
            stack.append(i % n)

        return res

    def trap(self, height: List[int]) -> int:
        # 单调栈 用行来计算雨水
        res = 0
        n = len(height)
        stack = [0]  # 存放下标
        for i in range(1, n):
            if height[i] == height[stack[-1]]:
                stack.pop()
            while stack and height[i] > height[stack[-1]]:
                mid = stack.pop()  # 凹槽中间 左为stack[-1] 右为i
                if stack:
                    h = min(height[i], height[stack[-1]]) - height[mid]
                    w = i - stack[-1] - 1
                    res += h * w
            stack.append(i)
        return res

    def largestRectangleArea(self, heights: List[int]) -> int:
        # 单调栈 递减栈
        heights.insert(0, 0)  # 头部加0，省去判断栈空
        heights.append(0)  # 尾部加0，最后一次必弹栈计算面积
        n = len(heights)
        res = 0
        stack = [0]
        for i in range(n):
            while heights[i] < heights[stack[-1]]:
                mid = stack.pop()  # 中间高两头低
                h = heights[mid]
                w = i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        return res

    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if n <= k:
            return '0'

        res = []
        stack = [num[0]]  # 递增栈
        nums = list(num)
        for i in range(1, n):
            while k > 0 and stack and nums[i] < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(nums[i])
        # 一直未弹栈，从后面开始弹
        while k > 0:
            stack.pop()
            k -= 1
        for i in range(len(stack)):
            if not res and i < len(stack) - 1 and stack[i] == '0':  # 前导0
                continue
            res.append(stack[i])
        return ''.join(res)

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        res = 0
        heights = [0] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] += 1
            # print(heights)
            res = max(res, self.largestRectangleArea(heights[:]))  # 值传递
        return res