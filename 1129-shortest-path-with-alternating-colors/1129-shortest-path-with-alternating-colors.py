class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        RED, BLUE = 1, 2
        graph = [[] for _ in range(n)]
        for i in range(len(redEdges)):
            u, v = redEdges[i]
            graph[u].append((v, RED))
        for i in range(len(blueEdges)):
            u, v = blueEdges[i]
            graph[u].append((v, BLUE))
        result = [-1]*n
        queue = deque([(0, 0)])
        distance = 0
        while queue:
            for _ in range(len(queue)):
                node, prevColor = queue.popleft()
                result[node] = distance
                for neigh, color in graph[node]:
                    if prevColor == 0 or prevColor != color:
                        queue.append((neigh, color))
            distance += 1
        return result
            
            