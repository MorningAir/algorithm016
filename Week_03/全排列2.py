class Solution:
    def permute(self, nums):
        ans = []
        used = [False for _ in range(len(nums))]
        nums.sort()
        def solve(cur):
            if len(cur) == len(nums):
                ans.append(cur[:])
                return
            for i in range(len(nums)):
                if used[i] == True or (i > 0 and nums[i] == nums[i - 1] and not used[i-1]):
                    continue
                used[i] = True
                solve(cur + [nums[i]])
                used[i] = False

        solve([])
        return ans
s = Solution()
print(s.permute([1,1,3]))