class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = ['' for _ in range(numRows)]
        down, row = -1, 0
        for i in range(len(s)):
            if i % (numRows - 1) == 0:
                down *= -1
            ans[row] += s[i]
            row += down
        return ''.join(ans)



