class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        def dp(i, j, lookUp=None):
            lookUp = {x: x for x in grid[n-1]} if lookUp is None else lookUp
            val = grid[i][j]
            if val in lookUp:
                return lookUp[val]
            lookUp[val] = float("inf")
            for k in range(m):
                temp = val + moveCost[val][k] + dp(i+1, k, lookUp)
                lookUp[val] = min(lookUp[val], temp)
            
            return lookUp[val]
            
        result = float("inf")
        for j in range(m):
            result = min(result, dp(0, j))
        
        return result
            