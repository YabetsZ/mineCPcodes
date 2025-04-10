class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        tGraph = [[] for _ in range(n+1)] # trusted by
        ttGraph = [[] for _ in range(n+1)] # trusts
        candidates = []

        for a, b in trust:
            tGraph[b].append(a)
            ttGraph[a].append(b)
            if len(tGraph[b]) == n-1:
                candidates.append(b)
        for x in candidates:
            if len(ttGraph[x]) == 0:
                return x
        return -1