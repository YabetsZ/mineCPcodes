class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visitedEdges = set()
        bestAnswer = {}
        def dfs(u):
            if u not in bestAnswer:
                bestAnswer[u] = 0
            for v, w in graph[u]:
                if (u, v) not in visitedEdges or bestAnswer[u] + w < bestAnswer[v] :
                    visitedEdges.add((u, v))
                    bestAnswer[v] = min(bestAnswer[u] + w, bestAnswer.get(v, float("inf")))
                    dfs(v)
        
        graph = [[] for _ in range(n+1)]
        for u, v, w in times:
            graph[u].append((v, w))
        dfs(k)
        return -1 if len(bestAnswer)!=n else max(bestAnswer.values())
        