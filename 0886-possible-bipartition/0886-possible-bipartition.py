class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(node):
            if node in visited:
                return True
            colored = Color[node] != -1
            if colored:
                color = Color[node]
                for neigh in Graph[node]:
                    if Color[neigh] != color:
                        Color[neigh] = 1 if color == 0 else 0
                    else:
                        return False
            else:
                Color[node] = 0
                for neigh in Graph[node]:
                    Color[neigh] = 1
            visited.add(node)
            for neigh in Graph[node]:
                res = dfs(neigh)
                if not res:
                    return False
            return True
        Color = [-1]*(n+1)
        Graph = [[] for _ in range(n+1)]
        visited = set()
        for u, v in dislikes:
            Graph[u].append(v)
            Graph[v].append(u)
        result = True
        for i in range(1, n+1):
            if i not in visited:
                result = result and dfs(i)

        return result
        