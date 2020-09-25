class Solution:
    def solve(self,nums,target):
        left = 0
        right = len(nums)-1
        nums.sort()
        while left<=right:
            mid = (right-left)//2+left
            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
            else:
                right = mid-1
        if left >=len(nums) or nums[left]!=target:
            return -1
        return left