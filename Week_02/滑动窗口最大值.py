class Solution:
    def maxSlidingWindow(self, nums, k):
        slide = []
        result = []
        for i in range(len(nums)):
            while slide and nums[slide[-1]]<nums[i]:
                slide.pop()
            slide.append(i)
            if slide[0] +k == i:
                slide.pop(0)
            result.append(nums[slide[0]])
        return result[k-1:]