'''
10.2 每日一题
405.十进制数转成十六进制数
'''

class Solution:
    def toHex(self, num: int) -> str:
        res = []
        # 负数 加上32位的偏移量
        if num < 0:
            num = num + 2 ** 32
        # 正数
        while num:
            reminder = num % 16
            if reminder < 10:
                res.append(chr(reminder + ord('0')))
            else:
                res.append(chr(reminder + ord('a') - 10))
            num //= 16
        # print(res)
        return ''.join(res[::-1]) if res else '0'