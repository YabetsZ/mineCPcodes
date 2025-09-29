class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def in_bound(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        
        def dp(i, j, memo=None):
            if memo is None:
                memo = {(0, 0) : grid[0][0]}
            if (i, j) not in memo:
                left = dp(i, j-1, memo) if in_bound(i, j-1) else float("inf")
                top = dp(i-1, j, memo) if in_bound(i-1, j) else float("inf")
                memo[(i, j)] = min(left, top) + grid[i][j]
            return memo[(i, j)]
        
        return dp(len(grid)-1, len(grid[0])-1)