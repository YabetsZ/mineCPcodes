class UnionFind:
    def __init__(self, size, count):
        self.parent = [i for i in range(size + 1)]  
        self.rank = [0] * (size + 1)
        self.components = size - count

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            self.components -= 1
            # print(self.parent)

class Solution:
    def regionsBySlashes(self, mat: List[str]) -> int:
        # Data representation: (0,0): blank, (0, 1):fSlash, (1, 0): bSlash
        def inbound(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid)
        n = len(mat)
        grid = [[1]*(2*n) for _ in range(2*n)]
        count = 0
        for i in range(n):
            for j in range(n):
                if mat[i][j] == "\\":
                    grid[2*i][2*j], grid[2*i+1][2*j+1] = 0, 0
                    count += 2
                elif mat[i][j] == "/":
                    grid[2*i+1][2*j], grid[2*i][2*j+1] = 0, 0
                    count += 2
        uf = UnionFind((2*n)**2, count)
        for i in range(2*n):
            for j in range(2*n):
                if grid[i][j] == 1:
                    for di, dj in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                        ni, nj = i+di, j+dj
                        if inbound(ni, nj) and grid[ni][nj] == 1:
                            uf.union(i*2*n+j, ni*2*n+nj)
        return uf.components