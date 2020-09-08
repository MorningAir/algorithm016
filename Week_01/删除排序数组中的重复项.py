class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        count = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            else:
                nums[count] = nums[i]
                count += 1
        return count
s = Solution()
print(s.removeDuplicates([1,1,2]))

