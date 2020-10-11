class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []

        def solve(nums, cur):
            if len(cur) > 1:
                result.append(cur)
            visited = set()
            for idx, n in enumerate(nums):
                if n in visited:
                    continue
                visited.add(n)
                if not cur or cur[-1] <= n:
                    solve(nums[idx + 1:], cur + [n])

        solve(nums, [])
        return result
