class Solution:
    def generateParenthesis(self, n):
        ans = []
        def solve(cur_str,left,right):
            if left ==0 and right == 0:
                ans.append(cur_str)
                return
            if left>right:
                return#剪枝
            if left>0:
                solve(cur_str+'(',left-1,right)
            if right>0:
                solve(cur_str+')',left,right-1)
        solve('',n,n)
        return ans
