'''
每日一题 9.1
165.比较版本号
'''
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')

        # 短的补0
        while len(v1) < len(v2):
            v1.append('0')
        while len(v2) < len(v1):
            v2.append('0')
        for i in range(len(v1)):
            if int(v1[i]) < int(v2[i]):
                return -1
            elif int(v1[i]) > int(v2[i]):
                return 1

        return 0


if __name__ == '__main__':
    version1 = '1.0.1'
    version2 = '1'

    solve = Solution()
    print(solve.compareVersion(version1, version2))
