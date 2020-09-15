class Solution:
    def numIslands(self, grid):
        def dfs(i, j):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == '0': return
            grid[i][j] = '0'
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != '0':
                    dfs(i, j)
                    count += 1
        return count
