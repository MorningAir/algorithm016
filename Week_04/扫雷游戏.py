class Solution:
    def updateBoard(self, board, click):
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        direction2 = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]

        def count(i, j):
            ans = 0
            for d in direction2:
                if 0 <= i + d[0] < len(board) and 0 <= j + d[1] < len(board[0]) and board[i + d[0]][j + d[1]] == 'M':
                    ans += 1
            return ans

        def solve(i, j):
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'E':
                if count(i, j) != 0:
                    board[i][j] = str(count(i, j))
                    return
                else:
                    board[i][j] = 'B'
                    for d in direction2:
                        solve(i + d[0], j + d[1])

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        else:
            solve(click[0], click[1])

        return board


s = Solution()
a = [["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","M"],["E","E","M","E","E","E","E","E"],["M","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","M","M","E","E","E","E"]]

b = [0,0]
print(s.updateBoard(a, b))
