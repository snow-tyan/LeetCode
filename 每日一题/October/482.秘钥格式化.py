'''
10.4 每日一题
482.密钥格式化
'''


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        n = len(s)
        res = []
        cnt = 0
        for i in range(n - 1, -1, -1):
            if cnt != 0 and cnt % k == 0 and res[-1] != '-':
                res.append('-')
            # 小写字母
            if ord('a') <= ord(s[i]) <= ord('z'):
                res.append(chr(ord(s[i]) - 32))
                cnt += 1
            elif s[i] != '-':
                res.append(s[i])
                cnt += 1
        if res and res[-1] == '-':
            res.pop()
        return ''.join(res[::-1])
