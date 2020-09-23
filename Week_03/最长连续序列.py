#暴力
#对于数字x，若x-1存在，则跳过，若X-1不存在说明可以作为起始点，开始遍历最长长度 最差是O(n^2)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        nums = set(nums)
        for i in nums:
            if i - 1 not in nums:
                LongestLength = 1
                while i + 1 in nums:
                    LongestLength += 1
                    i += 1
                result = max(result, LongestLength)
        return result



