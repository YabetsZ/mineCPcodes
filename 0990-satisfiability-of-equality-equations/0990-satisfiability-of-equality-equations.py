class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]  
        self.rank = [0] * (size + 1)  

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

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def equationsPossible(self, eqns: List[str]) -> bool:
        def calc(char):
            return ord(char) - ord('a')
        not_equal = []
        uf = UnionFind(26)

        for eqn in eqns:
            if eqn[1] == "=":
                uf.union(calc(eqn[0]), calc(eqn[-1]))
            else:
                not_equal.append([calc(eqn[0]), calc(eqn[-1])])
        
        for x, y in not_equal:
            if uf.connected(x, y):
                return False
        return True
