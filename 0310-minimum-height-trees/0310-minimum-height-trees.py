class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        indegree = [0]*n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        queue = deque()
        for i in range(n):
            if indegree[i] <= 1:
                queue.append(i)
        N = n
        while queue:
            if N <= 2:
                return list(queue)
            for _ in range(len(queue)):
                node = queue.popleft()
                N -= 1
                for neigh in graph[node]:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 1:
                        queue.append(neigh)

            