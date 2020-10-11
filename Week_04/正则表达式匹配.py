class Solution:
    def solve(self, s, p):
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(len(s) + 1):
            for j in range(1, len(p) + 1):
                if i == 0 and j >= 2 and p[j - 2] == '*':
                    dp[i][j] = dp[i][j - 2]
                elif j >= 2 and p[j - 1] == '*':
                    match = p[j - 2] == s[i - 1] or p[j - 1] == '.'
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and match)
                elif p[j - 1] != '*':
                    match = p[j - 1] == s[i - 1] or p[j - 1] == '.'
                    dp[i][j] = match and dp[i - 1][j - 1]
        return dp[-1][-1]


a = Solution()
s = 'aaa'
p = 'a*'
print(a.solve(s, p))
