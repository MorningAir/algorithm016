import copy
class Solution:
    def solveNQueens(self, n):
        ans = []
        cur = [['.' for _ in range(n)] for _ in range(n)]
        cols = [1 for _ in range(n)]
        duijiao1 = [1 for _ in range(2*(n-1)+1)]
        duijiao2 = [1 for _ in range(2*(n-1)+1)]
        def solve(row,cur):
            if row == n:
                result = []
                for i in cur:
                    string = ''.join(i)
                    result.append(string)
                ans.append(result)
                return
            for col in range(0,n):
                if cols[col] == 0 or duijiao1[row+col] == 0 or duijiao2[row-col+n-1] == 0:
                    continue
                cur[row][col] = 'Q'

                cols[col] = 0
                duijiao1[row+col] = 0
                duijiao2[row-col+n-1] = 0

                solve(row+1,cur)
                cur[row][col] = '.'
                cols[col] = 1
                duijiao1[row + col] = 1
                duijiao2[row - col + n - 1] = 1
        solve(0,cur)
        return ans
s = Solution()
print(s.solveNQueens(4))



