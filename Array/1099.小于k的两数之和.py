'''
双指针
1099.小于k的两数之和
259.较小的三数之和
611.有效三角形个数
15.三数之和
16.最接近的三数之和
1.两数之和
18.四数之和
'''
from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # 排序+二分
        # n = len(nums)
        # nums.sort()  # O(N*logN)
        # sum = 0
        # for i in range(n):  # O(N*logN)
        #     left, right = i + 1, n - 1
        #     j = i
        #     while left <= right:
        #         mid = (left + right) // 2
        #         if nums[i] + nums[mid] < k:
        #             j = mid
        #             left = mid + 1
        #         else:
        #             right = mid - 1
        #     if j != i:
        #         sum = max(sum, nums[i] + nums[j])
        #     elif sum == 0:
        #         return -1
        # return sum

        n = len(nums)
        nums.sort()  # O(N*logN)
        print(nums)  # [1, 8, 23, 24, 33, 34, 54, 75]
        res = 0
        # 双指针 O(N)
        i, j = 0, n - 1
        while i < j:
            if nums[i] + nums[j] < k:
                res = max(res, nums[i] + nums[j])
                i += 1
            else:
                j -= 1
        return res if res > 0 else -1

    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # 排序+二分 O(N^2logN)
        # n = len(nums)
        # nums.sort()  # O(N*logN)
        # res = 0
        # # 二重二分查找O(N^2*logN)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         left, right, k = j + 1, n - 1, j
        #         while left <= right:
        #             mid = (left + right) // 2
        #             if nums[i] + nums[j] + nums[mid] < target:
        #                 k = mid
        #                 left = mid + 1
        #             else:
        #                 right = mid - 1
        #         res += k - j
        # return res

        n = len(nums)
        nums.sort()  # O(N*logN)
        # print(nums)
        res = 0  # 记录满足条件的个数
        # 枚举i，让j和k双指针遍历数组 O(N^2)
        for i in range(n):
            j, k = i + 1, n - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < target:
                    res += k - j  # 将区间[j+1,k]整个计入答案
                    j += 1
                else:
                    k -= 1
        return res

    def triangleNumber(self, nums: List[int]) -> int:
        # 三角形：任意两边大于第三边 即
        # a+b>c a+c>b b+c>a 同时成立
        # 排序 天然有a<=b<=c 必有 a+c>b b+c>a 故
        # 只需保证 a+b>c
        # 方法一：排序+二分
        # n = len(nums)
        # nums.sort()
        # res = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         # 二分查找
        #         left, right = j + 1, n - 1
        #         upper = j  # 区间上界
        #         while left <= right:
        #             mid = (left + right) // 2
        #             if nums[i] + nums[j] > nums[mid]:
        #                 upper = mid
        #                 left = mid + 1
        #             else:
        #                 right = mid - 1
        #         res += upper - j
        # return res

        # 方法二：排序+双指针
        n = len(nums)
        nums.sort()  # [2,2,3,4]
        res = 0
        # 枚举最长边c，双指针j k遍历数组一遍
        for i in range(n - 1, 1, -1):  # 从后往前枚举[n-1, 2]
            j, k = 0, i - 1
            while j < k:
                if nums[i] < nums[j] + nums[k]:
                    res += max(k - j, 0)
                    k -= 1
                else:
                    j += 1

        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        # # 枚举中间的数
        # for i in range(1, n - 1):
        #     j, k = 0, n - 1
        #     while j < i < k:
        #         if nums[i] + nums[j] + nums[k] > 0:  # 如果大于0，大数调小
        #             k -= 1
        #         else:
        #             if nums[i] + nums[j] + nums[k] == 0 and [nums[i], nums[j], nums[k]] not in res:
        #                 res.append([nums[i], nums[j], nums[k]])
        #             j += 1
        # return res

        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:  # 避免重复解
                continue
            j, k = i + 1, n - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:  # 避免重复解
                        j = j + 1
                    while j < k and nums[k] == nums[k - 1]:  # 避免重复解
                        k = k - 1
                    j = j + 1  # 双指针同时往中间移动，也是避免重复解
                    k = k - 1
                elif nums[i] + nums[j] + nums[k] > 0:  # 大了，大数左移
                    k = k - 1
                else:  # 小了，小数右移
                    j = j + 1
        return res

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 题意：只存在唯一解
        n = len(nums)
        nums.sort()
        res = 0
        limit = 3e3
        # 枚举小数
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # 避免重复解
                continue
            j, k = i + 1, n - 1
            while j < k:
                sum3 = nums[i] + nums[j] + nums[k]
                if abs(sum3 - target) < limit:
                    limit = abs(sum3 - target)
                    res = sum3
                if sum3 == target:
                    # 唯一解
                    return target
                elif sum3 > target:  # 大了，大数左移
                    while j < k and nums[k] == nums[k - 1]:  # 避免重复解
                        k = k - 1
                    k = k - 1
                else:  # 小了，小数右移
                    while j < k and nums[j] == nums[j + 1]:  # 避免重复解
                        j = j + 1
                    j = j + 1

        return res

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}  # {nums[i]:i}
        for i, num in enumerate(nums):
            # 查表
            if target - num in hashtable:
                return [hashtable[target - num], i]
            # 更新表
            hashtable[num] = i
        return []

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        # print(nums)  # [-2, -1, 0, 0, 1, 2]
        res = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
                    else:
                        left += 1
        return res


solve = Solution()
# nums = [-1, 0, 1, 2, -1, -4]
# print(solve.threeSum(nums))
# nums = [-100, -98, -2, -1]
# target = -101
# print(solve.threeSumClosest(nums, target))
