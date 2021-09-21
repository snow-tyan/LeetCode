'''
49.字母异位词分组
'''
from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 方法一：排序后结果作为key，原串作为val
        # 方法二：计数 每个字母出现次数，tuple作为key，原串作为val
        mp = collections.defaultdict(list)  # 默认value为list类型

        # for st in strs:
        #     key = ''.join(sorted(st))
        #     mp[key].append(st)

        for st in strs:
            alpha = [0] * 26
            for ch in st:
                alpha[ord(ch) - ord('a')] += 1
            key = tuple(alpha)
            mp[key].append(st)

        return list(mp.values())
