class Solution:
    def moveZeroes(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[j] = nums[i]
                if i!=j:
                    nums[i] = 0
                j +=1
s = Solution()
input = [0,1,0,3,12]
s.moveZeroes(input)
print(input)

