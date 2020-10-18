class Solution:
    def numDecodings(self, s):
        result = [0 for _ in range(len(s)+1)]
        result[0] = 1
        for i in range(1,len(s)+1):
            if s[i-1] != '0':
                result[i] +=result[i-1]
            if i>=2 and 10 <= int(s[i-2:i]) <= 26:
                result[i] += result[i-2]
        return result[-1]