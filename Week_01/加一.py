class Solution:
    def plusOne(self, digits):
        start = len(digits)-1
        while digits[start]==9:
            digits[start] = 0
            start -=1
        if start == -1:
            digits = [1] + digits
        else:
            digits[start] +=1
        return digits
s = Solution()
print(s.plusOne([9,9,9]))



