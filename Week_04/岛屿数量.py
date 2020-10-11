class Solution:
    def numIslands(self, grid):
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j):
            grid[i][j] = '0'
            for dire in direction:
                new_i, new_j = i + dire[0], j + dire[1]
                if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] == '1':
                    dfs(new_i, new_j)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count
