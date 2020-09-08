class Solution:
    def trap(self, height):
        stack = []  # 维护一个单调递减栈，不严格
        ans = 0
        for i in range(len(height)):
            while stack and height[i]>height[stack[-1]]:
                cur = stack.pop()
                if not stack:
                    break
                w = i - stack[-1]-1
                h = min(height[i],height[stack[-1]])-height[cur]
                ans+=w*h
            stack.append(i)
        return ans

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
