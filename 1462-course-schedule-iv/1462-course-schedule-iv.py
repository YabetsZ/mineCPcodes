class Solution:
    def checkIfPrerequisite(self, n: int, prereq: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(n)]
        queue = deque()
        isDecendant = [[0] * n for _ in range(n)]
        for i in range(len(prereq)):
            u, v = prereq[i]
            graph[u].append(v)
        def bfs(node):
            queue = deque([node])
            while queue:
                for i in range(len(queue)):
                    course = queue.popleft()
                    if course != node:
                        isDecendant[node][course] = 1
                    for nekst in graph[course]:
                        queue.append(nekst)
        for i in range(n):
            bfs(i)
        result = []
        for u, v in queries:
            if isDecendant[u][v] == 1:
                result.append(True)
            else:
                result.append(False)
        return result