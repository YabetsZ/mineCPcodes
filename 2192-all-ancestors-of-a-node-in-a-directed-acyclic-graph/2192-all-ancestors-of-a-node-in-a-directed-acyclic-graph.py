class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def dfs(i, arr):
            if len(arr) != 0:
                # insert_unique_sorted_list(result[i], arr)
                result[i].extend(arr)
            arr.append(i)
            for neigh in graph[i]:
                dfs(neigh, arr)
            arr.pop()

        graph = [[] for _ in range(n)]
        inDegree = [False]*n
        for u, v in edges:
            graph[u].append(v)
            inDegree[v] = True
        
        result = [[] for _ in range(n)]
        visited = set()
        for i in range(n):
            if not inDegree[i]:
                dfs(i, [])
        for i in range(n):
            result[i] = sorted(set(result[i]))
        return result
