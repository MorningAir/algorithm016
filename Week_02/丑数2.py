class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2,i3,i5 = 0,0,0
        for _ in range(n-1):
            cur = min(ugly[i2]*2,ugly[i3]*3,ugly[i5]*5)
            if cur == ugly[i2]*2:
                i2+=1
            if cur == ugly[i3]*3:
                i3+=1
            if cur == ugly[i5]*5:
                i5+=1
            ugly.append(cur)
        return ugly[-1]

