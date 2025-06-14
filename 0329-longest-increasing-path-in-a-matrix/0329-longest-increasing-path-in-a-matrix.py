class Solution:
    def longestIncreasingPath(self, mat: List[List[int]]) -> int:
        drxn = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        def inbound(i, j):
            return 0 <= i < len(mat) and 0 <= j < len(mat[0])
        @lru_cache(maxsize=None)
        def dfs(i, j):
            result = 0
            for di, dj in drxn:
                ni, nj = i+di, j+dj
                if inbound(ni, nj) and mat[ni][nj] > mat[i][j]:
                    result = max(dfs(ni, nj), result)

            return result + 1
        result = -float("inf")
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                result = max(result, dfs(i, j))
            
        return result
            