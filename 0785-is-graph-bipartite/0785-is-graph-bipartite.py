class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # red, blue = 0, 1
        colors = [-1]*(len(graph))
        def bfs(node):
            queue = deque([node])
            colors[node] = 0
            while queue:
                i = queue.popleft()
                color = colors[i]
                for n in graph[i]:
                    if colors[n] != -1 and colors[n] != 1-color:
                        return False
                    if colors[n] == -1:
                        colors[n] = 1-color
                        queue.append(n)
            return True
        for i in range(len(graph)):
            if colors[i] == -1:
                if not bfs(i):
                    return False
        return True
            

