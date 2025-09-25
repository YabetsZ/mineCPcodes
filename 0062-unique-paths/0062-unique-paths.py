class Solution:
    def uniquePaths(self, n: int, m: int) -> int:
        grid = [[0]*m for _ in range(n)]
        grid[0][0] = 1
        for i in range(n):
            for j in range(m):
                if j != m-1:
                    grid[i][j+1] += grid[i][j]
                if i != n-1:
                    grid[i+1][j] +=  grid[i][j]
    
        return grid[-1][-1]