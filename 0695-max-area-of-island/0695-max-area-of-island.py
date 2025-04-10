class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def in_bound(row, col):
            return (0 <= row <= len(grid)-1 and 0 <= col <= len(grid[0])-1)
        def dfs(row, col):
            count = 1
            visited.add((row, col))

            for dy, dx in drxn:
                if in_bound(row+dy, col+dx) and (row+dy, col+dx) not in visited and grid[row+dy][col+dx] == 1:
                    count += dfs(row+dy, col+dx)
            return count
        maxArea = 0
        drxn = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        n, m = len(grid), len(grid[0])
        visited = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in visited:
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea