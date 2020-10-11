class Solution:
    def findMin(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        if nums[0] < nums[right]:
            return nums[0]
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

