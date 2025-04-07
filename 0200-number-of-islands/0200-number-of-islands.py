class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        drxn = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        def in_bound(row, col):
            return (0 <= row <= len(grid)-1 and 0 <= col <= len(grid[0])-1)
        def count():
            res = 0
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if (row, col) not in visited and grid[row][col] == "1":
                        # print("here")  
                        dfs(row, col)
                        res += 1
            return res
        def dfs(row, col):
            # print("here")
            visited.add((row, col))

            for dy, dx in drxn:
                if in_bound(row+dy, col+dx) and (row+dy, col+dx) not in visited and grid[row+dy][col+dx] == "1":
                    dfs(row+dy, col+dx)
        return count()
