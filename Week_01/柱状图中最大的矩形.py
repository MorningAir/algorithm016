class Solution:
    def largestRectangleArea(self, heights):
        heights.append(0)
        stack = [-1]
        maxarea = 0
        for i in range(len(heights)):
            while heights[i]<heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] -1
                maxarea = max(maxarea,h*w)
            stack.append(i)
        return maxarea