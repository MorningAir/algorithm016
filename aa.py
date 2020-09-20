class Solution:
    def subsets(self, nums):
        res = [[]]
        for i in nums:
            for j in res[:]:
                res += [j + [i]]
        return res


s = Solution()
print(s.subsets([1, 2, 3]))
