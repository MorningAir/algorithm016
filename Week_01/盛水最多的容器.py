class Solution:
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        result = 0
        while i < j:
            if height[i] < height[j]:
                result = max((j - i) * height[i], result)
                i += 1
            else:
                result = max((j - i) * height[j], result)
                j -= 1
        return result

s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
