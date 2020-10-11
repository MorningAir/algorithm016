class Solution:
    def subsets(self, nums):
        ans = []
        n = len(nums)
        def solve(cur_str,cur_index):
            ans.append(cur_str)
            for i in range(cur_index,n):
                cur_str = cur_str+[nums[i]]
                solve(cur_str,i+1)
                cur_str = cur_str[:-1]
        solve([],0)
        return ans
s = Solution()
print(s.subsets([1,2,3]))


