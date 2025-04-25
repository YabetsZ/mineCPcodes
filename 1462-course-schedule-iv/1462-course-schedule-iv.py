class Solution:
    # def checkIfPrerequisite(self, n: int, prereq: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # graph = [[] for _ in range(n)]
        # isDecendant = [set() for _ in range(n)]
        # inDegree = [0] * n
        # for i in range(len(prereq)):
        #     u, v = prereq[i]
        #     graph[u].append(v)
        #     inDegree[v] += 1
        # def dfs(node):
        #     if len(isDecendant[node]) != 0:
        #         return set([node]).union(isDecendant[node])
        #     decendant = set()
        #     for neigh in graph[node]:
        #         decendant.update(dfs(neigh))
        #     isDecendant[node] = decendant.copy()
        #     decendant.add(node)
        #     return decendant
        # for i in range(n):
        #     if inDegree[i] == 0:
        #         dfs(i)
        # result = []
        # for u, v in queries:
        #     if v in isDecendant[u]:
        #         result.append(True)
        #     else:
        #         result.append(False)
        # return result
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        reach = {}
        adj = [[] for _ in range(numCourses)]
        for x in prerequisites:
            adj[x[1]].append(x[0])
        res = []
        for i,x in enumerate(queries):
            st = x[1]
            q = deque([st])
            vis = set()
            vis.add(st)
            while(q):
                cur = q.popleft()
                for l in adj[cur]:
                    if l==x[0]:
                        res.append(True)
                        q = deque([])
                        break
                    if l not in vis:
                        vis.add(l)
                        q.append(l)
            if len(res)<i+1:
                res.append(False)
        return res