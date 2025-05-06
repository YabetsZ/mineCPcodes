class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]  
        self.rank = [0] * (size + 1)
        self.components = size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y): # z = (x, y)
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

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        components = len(stones)

        x_set = defaultdict(int)
        y_set = defaultdict(int)
        uf = UnionFind(components)
        for i in range(components):
            x, y = stones[i]
            if x in x_set:
                uf.union(i, x_set[x])
            if y in y_set:
                uf.union(i, y_set[y])
            if y not in y_set or x not in x_set:
                x_set[x] = i
                y_set[y] = i
        return len(stones) - uf.components
        