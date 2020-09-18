class Solution:
    def myPow(self, x, n):
        if n ==0:
            return 1
        elif n>0:
            if n%2 == 1:
                return self.myPow(x*x,n//2)*x
            else:
                return self.myPow(x*x,n//2)
        else:
            return 1.0/self.myPow(x,-n)

s = Solution()
print(s.myPow(2.000, 3))
