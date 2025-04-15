class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        def inBound(i, j):
            nonlocal n, m
            return 0 <= i < n and 0 <= j < m

        queue = deque()
        count = 0
        visited = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))
                    visited.add((i,j))
        minutes = 0
        while queue:
            increment = False
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni, nj = i+dy, j+dx
                    if inBound(ni, nj) and (ni, nj) not in visited and grid[ni][nj] == 1:
                        queue.append((ni,nj))
                        visited.add((ni, nj))
                        count -= 1
                        increment = True
            if increment:
                minutes += 1
        
        
        return minutes if count == 0 else -1
        