class Solution:
    def maxProfit(self, prices):
        ans = 0
        for i in range(1,len(prices)):
            temp = prices[i] - prices[i-1]
            if temp>0:
                ans += temp
        return ans
