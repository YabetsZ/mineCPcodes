class Solution:
    def maximalSquare(self, mat: List[List[str]]) -> int:
        n, m = len(mat), len(mat[0])
        pre = [[0]*(m+1)]
        for i in range(n):
            pre.append([0])
            for j in range(m):
                ni, nj = i+1, j+1
                pre[ni].append(int(mat[i][j]) + pre[ni][-1] + pre[ni-1][nj] - pre[ni-1][nj-1])
        
        def inbound(i, j):
            return 1 <= i < n+1 and 1 <= j < m+1
        def check_square(i1, j1, i2, j2):
            sum_square = pre[i2][j2] - pre[i2][j1-1] - pre[i1-1][j2] + pre[i1-1][j1-1]
            return sum_square == (j2-j1+1)*(i2-i1+1)
        
        result = 0
        for i1 in range(1, n+1):
            for j1 in range(1, m+1):
                if min(m+1-j1, n+1-i1) <= result**0.5: continue
                i2, j2 = i1, j1
                while inbound(i2, j2) and check_square(i1, j1, i2, j2):
                    result = max(result, (j2-j1+1)*(i2-i1+1))
                    print(result, i1, j1)
                    i2, j2 = i2+1, j2+1
        
        return result


