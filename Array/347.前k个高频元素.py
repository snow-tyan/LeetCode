'''
堆
剑指offer40.最小的k个数
215.数组中的第k个最大元素
347.前k个高频元素
# 295.数据流的中位数
# 239.滑动窗口最大值 堆/单调队列
'''
from typing import List
import collections
import heapq

'''
heap queue 小顶堆
若需要大顶堆， heapq.heappush(heap, -elem) -heapq.heappop(heap)
heapq.heapify(heap)         O(N)  自底向上式建堆
heapq.heappush(heap, item)  O(logN)
heapq.heappop(heap)         O(1)
heap[0]                     O(1)
heapq.heappushpop(heap, item)  item先入堆再弹堆顶元素
heapq.heapreplace(heap, item)  先弹堆顶元素item再入堆
常用操作：
    if item > heap[0]:
        item = heapreplace(heap, item)
'''


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # 如果是一个一个元素入堆   O(NlogN)  (自顶向下)
        # 维护容量为k的大顶堆     O(NlogK)
        heapq.heapify(arr)  # O(N)将arr原地heap化 (自底向上式建堆)
        # print(arr)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(arr))
        return res

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # # 小顶堆
        # n = len(nums)
        # heapq.heapify(nums)  # 原地建堆 O(N) 自底向上
        # for _ in range(n - k + 1):
        #     res = heapq.heappop(nums)  # O((N-K+1)log(N-K+1))
        # return res

        # # 大顶堆
        # heap = []
        # for num in nums:
        #     heapq.heappush(heap, -num)  # 建堆 O(NlogN)
        # for _ in range(k):
        #     res = -heapq.heappop(heap)  # O(KlogK)
        # return res

        # 维护容量为k的小顶堆
        heap = []
        n = len(nums)
        for i in range(k):
            heapq.heappush(heap, nums[i])  # 建堆 O(KlogK)
        for i in range(k, n):  # 循环维护堆 O((N-K)log(N-K))
            if nums[i] > heap[0]:
                temp = heapq.heapreplace(heap, nums[i])  # 先弹堆顶再入堆
        return heap[0]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 遍历一遍数组，计数频率
        # 建堆，维护容量为k的小顶堆
        # 返回heap即可 (TopK)
        cnt = collections.Counter(nums)
        heap = []
        res = []
        for key, val in cnt.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))  # tuple
                continue
            if val > heap[0][0]:
                heapq.heappushpop(heap, (val, key))
        for h in heap:
            res.append(h[1])
        return res


solve = Solution()
# print(solve.getLeastNumbers([0, 1, 2, 1], 1))
print(solve.topKFrequent([1, 1, 1, 2, 2, 3], 2))
