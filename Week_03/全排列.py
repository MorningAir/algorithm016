class Solution:
    def permute(self, nums):
        ans = []
        used = [False for _ in range(len(nums))]

        def solve(cur):
            if len(cur) == len(nums):
                ans.append(cur)
            for i in range(len(nums)):
                if used[i] == True:
                    continue
                used[i] = True

                solve(cur+[nums[i]])
                used[i] = False
        solve([])
        return ans
s = Solution()
print(s.permute([1,2,3]))