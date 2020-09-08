class Solution:
    def twoSum(self, nums, target):
        need = {}
        for i in range(len(nums)):
            if nums[i] in need:
                return [need[nums[i]],i]
            else:
                need[target-nums[i]] = i
s = Solution()
print(s.twoSum([2,7,11,15],9))
