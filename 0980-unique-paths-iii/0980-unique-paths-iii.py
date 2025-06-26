class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        drxn = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        empties, start = 0, None
        for i in range(n):
            for j in range(m):
                val = grid[i][j]
                if val == 0:
                    empties += 1
                elif val == 1:
                    start = (i, j)
        self.result = 0
        visited = set()
        def inbound(i, j):
            return 0 <= i < n and 0 <= j < m
        
        def dfs(i, j):
            if grid[i][j] == 2:
                if len(visited) == empties + 1:
                    self.result += 1
                return
            visited.add((i, j))
            for di, dj in drxn:
                ni, nj = i+di, j+dj
                if inbound(ni, nj) and (ni, nj) not in visited and grid[ni][nj] != -1:
                    dfs(ni, nj)
            visited.discard((i, j))
        
        dfs(*start)
        return self.result

