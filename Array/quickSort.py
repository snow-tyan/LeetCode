'''
三大排序
quickSort
quickSort 非递归
mergeSort
heapSort
'''
from typing import List


class Solution:
    def quickSort(self, nums: List[int], left: int, right: int) -> None:
        if left >= right:
            return
        pivot = left
        mark = nums[left]
        for i in range(left + 1, right + 1):
            if nums[i] < mark:
                pivot += 1
                nums[i], nums[pivot] = nums[pivot], nums[i]  # swap
        nums[left], nums[pivot] = nums[pivot], nums[left]
        self.quickSort(nums, left, pivot - 1)
        self.quickSort(nums, pivot + 1, right)

    def quickSortBFS(self, nums: List[int], left: int, right: int) -> None:
        stack = [(left, right)]
        while stack:
            left, right = stack.pop()
            if left >= right:
                continue
            pivot = left
            mark = nums[left]
            for i in range(left, right + 1):
                if nums[i] < mark:
                    pivot += 1
                    nums[i], nums[pivot] = nums[pivot], nums[i]  # swap
            nums[left], nums[pivot] = nums[pivot], nums[left]
            stack.append((left, pivot - 1))
            stack.append((pivot + 1, right))

    def mergeSort(self, nums: List[int], temp: List[int], left: int, right: int) -> None:
        if left >= right:
            return
        mid = left + (right - left) // 2
        self.mergeSort(nums, temp, left, mid)
        self.mergeSort(nums, temp, mid + 1, right)

        i, j, k = left, mid + 1, 0
        while i <= mid and j <= right:
            if nums[i] < nums[j]:
                temp[k] = nums[i]
                i += 1
                k += 1
            else:
                temp[k] = nums[j]
                j += 1
                k += 1
        while i <= mid:
            temp[k] = nums[i]
            i += 1
            k += 1
        while j <= right:
            temp[k] = nums[j]
            j += 1
            k += 1
        k = 0
        for i in range(left, right + 1):
            nums[i] = temp[k]
            k += 1

    def heapSort(self, nums: List[int]):
        def adjustHeap(nums: List[int], parent: int, length: int) -> None:
            son = 2 * parent + 1
            while son < length:
                if son + 1 < length and nums[son] < nums[son + 1]:
                    son += 1
                if nums[son] < nums[parent]:
                    break
                nums[son], nums[parent] = nums[parent], nums[son]  # swap
                parent = son
                son = 2 * parent + 1

        # bulid heap
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            adjustHeap(nums, i, n)
        # swap
        nums[0], nums[n - 1] = nums[n - 1], nums[0]
        for i in range(1, n):
            adjustHeap(nums, 0, n - i)
            nums[0], nums[n - i - 1] = nums[n - i - 1], nums[0]


if __name__ == '__main__':
    solve = Solution()
    nums = [47, 22, 33, 49, 33, 12, 68, 29]
    print(nums)
    # solve.quickSort(nums, 0, len(nums) - 1)
    # solve.quickSortBFS(nums, 0, len(nums) - 1)
    temp = [0] * len(nums)
    # solve.mergeSort(nums, temp, 0, len(nums) - 1)
    solve.heapSort(nums)
    print(nums)
