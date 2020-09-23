class Solution:
    def twoSum(self, n):

        dp = [0 for _ in range(6 * n + 1)]
        for i in range(1, 7):
            dp[i] = 1

        for i in range(2, n + 1):
            for j in range(i * 6, 0, -1):
                dp[j] = 0
                for k in range(1, 7):
                    if j >= k + 1:
                        dp[j] += dp[j - k]
        res = []
        for i in range(n, n * 6 + 1):
            res.append(dp[i] / 6 ** n)
        return res