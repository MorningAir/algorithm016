class Solution:
    def climbStairs(self, n):
        if n <= 3:
            return n
        f1, f2 = 2, 3
        for i in range(4, n + 1):
            f3 = f1 + f2
            f1, f2 = f2, f3
        return f3
