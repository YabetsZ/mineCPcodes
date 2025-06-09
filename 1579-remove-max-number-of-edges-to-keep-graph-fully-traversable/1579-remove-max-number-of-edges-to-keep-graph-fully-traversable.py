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

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def process(person, u, v):
            if not person.connected(u, v):
                person.union(u, v)
            else:
                self.remove_count += 1
        alice, bob = UnionFind(n), UnionFind(n)
        alice_path, bob_path = [],[]
        self.remove_count = 0
        for t, u, v in edges:
            if t == 2:
                bob_path.append((u, v))
            elif t == 1:
                alice_path.append((u, v))
            else:
                if not alice.connected(u, v):
                    alice.union(u, v)
                    bob.union(u, v)
                else:
                    self.remove.count += 1

        while alice_path or bob_path:
            if alice_path:
                u, v = alice_path.pop()
                process(alice, u, v)
            if bob_path:
                u, v = bob_path.pop()
                process(bob, u, v)
                
        if bob.components != 1 or alice.components != 1:
            return -1
        return self.remove_count
            