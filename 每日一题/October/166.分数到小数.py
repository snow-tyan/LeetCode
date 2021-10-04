'''
10.3 每日一题
166.分数到小数
'''
import collections


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # 拆解为：
        # 1 计算正负号
        # 2 计算整数部分
        # 3 计算小数部分 有限小数/无限循环小数

        bit = numerator * denominator
        res = []
        if bit == 0:
            return '0'
        if bit < 0:
            res.append('-')
        num, den = abs(numerator), abs(denominator)
        # 整数部分
        integer = num // den
        res.append(str(integer))
        # 整除
        if num % den == 0:
            return ''.join(res)
        # 未被整除，计算小数部分
        res.append('.')
        num = num - (num // den) * den
        index = len(res)
        pos = collections.defaultdict()  # 存储之前出现过的分子的下标
        # 如果是有限小数，最终会整除即num会等于0
        while num and num not in pos.keys():
            pos[num] = index
            index += 1
            num *= 10  # 分子*10
            res.append(str(num // den))  # 分子/分母
            num = num - (num // den) * den
        # 无限循环小数
        if num != 0:
            last_pos = pos[num]
            loop = ['(']
            loop.extend(res[last_pos:])  # 循环部分
            loop.append(')')
            res = res[:last_pos]
            res.extend(loop)
        return ''.join(res)
