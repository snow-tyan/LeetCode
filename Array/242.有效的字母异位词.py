'''
哈希
242.有效的字母异位词
383.赎金信
49.字母异位词分组
438.找到字符串中所有字母异位词
349.两个数组的交集
350.两个数组的交集II
202.快乐数
454.四数相加II
'''
from typing import List
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alpha = [0] * 26
        for ch in s:
            alpha[ord(ch) - ord('a')] += 1

        for ch in t:
            alpha[ord(ch) - ord('a')] -= 1

        for i in range(26):
            if alpha[i] != 0:
                return False
        return True

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt_note = collections.Counter()
        for ch in ransomNote:
            cnt_note[ch] += 1
        for ch in magazine:
            if ch in cnt_note.keys():
                cnt_note[ch] -= 1
                if cnt_note[ch] == 0:
                    cnt_note.pop(ch)
        return True if not cnt_note else False

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key各字母次数 val同组异位词列表
        mp = collections.defaultdict(list)
        for s in strs:
            alpha = [0] * 26
            for ch in s:
                alpha[ord(ch) - ord('a')] += 1
            key = tuple(alpha)
            mp[key].append(s)
        return list(mp.values())

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        res = set()
        for num in nums2:
            if num in set1:
                res.add(num)
        return list(res)

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 进阶
        # 若两数组有序，用双指针分别指向数组头，若相等则加入答案，每次移动较小元素的数组指针
        # 若数组有序；一个数组很短很小；内存有限不能一次存一个数组 双指针法更优
        res = []
        cnt1 = collections.Counter(nums1)
        for num in nums2:
            if cnt1[num]:
                res.append(num)
                cnt1[num] -= 1
        return res

    def isHappy(self, n: int) -> bool:
        def get_sum(n: int) -> int:
            sum = 0
            while n:
                sum += (n % 10) * (n % 10)
                n //= 10
            return sum

        # # 方法一：打表 若出现在表中，则会进入死循环
        # table = set()
        # while n != 1:
        #     n = get_sum(n)
        #     if n in table:
        #         return False
        #     table.add(n)
        # return True

        # 方法二：快慢指针 快慢指针相遇则有环
        slow = n
        fast = get_sum(n)

        while fast != 1 and slow != fast:
            slow = get_sum(slow)
            fast = get_sum(get_sum(fast))
        # 若能走到1，必是fast先到
        return True if fast == 1 else False

    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # a+b+c+d=0 即a+b=-(c+d)
        # 遍历nums1 nums2 统计{a+b: 次数}
        # 遍历nums3 nums4数组，找到 -(c+d) 字典中出现过的次数

        mp = collections.Counter()
        cnt = 0
        for a in nums1:
            for b in nums2:
                mp[a + b] += 1

        for c in nums3:
            for d in nums4:
                key = -(c + d)
                cnt += mp[key]
        return cnt


solve = Solution()
print(solve.isHappy(19))
