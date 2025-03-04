class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        horizontal_max = [0] * n
        vertical_max = [0] * n
        for j in range(n):
            for i in range(n):
                vertical_max[j] = max(vertical_max[j], grid[i][j])
                horizontal_max[i] = max(horizontal_max[i], grid[i][j])
        result = 0
        for i in range(n):
            for j in range(n):
                result += min(horizontal_max[i], vertical_max[j]) - grid[i][j]
        return result
