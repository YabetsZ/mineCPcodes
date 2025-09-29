class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def in_bound(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        n, m = len(grid), len(grid[0])
        # recursive version
        def dp_recursive(i, j, memo=None):
            if memo is None:
                memo = {(0, 0) : grid[0][0]}
            if (i, j) not in memo:
                left = dp(i, j-1, memo) if in_bound(i, j-1) else float("inf")
                top = dp(i-1, j, memo) if in_bound(i-1, j) else float("inf")
                memo[(i, j)] = min(left, top) + grid[i][j]
            return memo[(i, j)]
        # return dp_recursive(len(grid)-1, len(grid[0])-1)
        table = [[float("inf")]*m for _ in range(n)]
        table[0][0] = grid[0][0]
        for i in range(n):
            for j in range(m):
                if i + 1 < n:
                    table[i+1][j] = min(table[i][j] + grid[i+1][j], table[i+1][j])
                if j + 1 < m:
                    table[i][j+1] = min(table[i][j] + grid[i][j+1], table[i][j+1])
        
        return table[-1][-1]