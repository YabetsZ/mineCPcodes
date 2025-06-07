class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]  
        self.rank = [0] * (size + 1)  
        self.components = size

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

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n, l = len(strs), len(strs[0])
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i+1, n):
                if sum([1 for k in range(l) if strs[i][k] != strs[j][k]]) <= 2:
                    uf.union(i, j)
        
        return uf.components
