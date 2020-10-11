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
        if left >=len(nums) or nums[left]!=target:#左指针是否在数组范围内，且等于target
            return -1
        return left#求左边界就返回左指针，判断左指针是否合法