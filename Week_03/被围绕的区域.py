class Solution:
    def solve(self, board):
        self.direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
        self.board = board
        if not self.isValid(board): return []
        rows, cols = len(board), len(board[0])
        for col in range(cols):
            self.dfs(0, col, rows, cols)
            self.dfs(rows - 1, col, rows, cols)
        for row in range(rows):
            self.dfs(row, 0, rows, cols)
            self.dfs(row, cols - 1, rows, cols)
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == '-':
                    board[row][col] = 'O'
                elif board[row][col] == 'O':
                    board[row][col] = 'X'
        return board

    def dfs(self, row, col, rows, cols):  # 遍历本身和周围的O，改成’-‘
        if row >= rows or row < 0 or col >= cols or col < 0 or self.board[row][col] != 'O':
            return
        else:
            self.board[row][col] = '-'
            for direc in self.direction:
                new_row = row + direc[0]
                new_col = col + direc[1]
                self.dfs(new_row, new_col, rows, cols)

    def isValid(self, board):
        if len(board) == 0:
            return False
        else:
            return True


s = Solution()
board = [["X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X"], ["X", "O", "X", "O", "X", "O"],
         ["O", "X", "O", "X", "O", "X"]]
print(s.solve(board))
