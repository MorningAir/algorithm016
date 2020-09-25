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
                left = mid+1
        if right <0 or nums[right]!=target:
            return -1
        return right