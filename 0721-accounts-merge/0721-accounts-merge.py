class UnionFind:
    def __init__(self, size, accounts):
        self.size = size
        self.parent = [i for i in range(size + 1)] 
        self.accounts = accounts
        self.seenEmails = {}
        self.result = defaultdict(set)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, idx):
        if x in self.seenEmails:
            self.parent[idx] = self.seenEmails[x]
        else:
            self.seenEmails[x] = self.parent[idx]
     
    def merge(self):
        merged = []
        for key, val in self.seenEmails.items():
            pIdx = self.find(val)
            self.result[pIdx].add(key)
        for key, val in self.result.items():
            merged.append([self.accounts[key][0]] + sorted(list(val)))
        return merged
            

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts), accounts)
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                uf.union(accounts[i][j], i)

        return uf.merge()
