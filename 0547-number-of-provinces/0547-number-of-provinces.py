class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            visited.add(node)
            for neigh in Graph[node]:
                if neigh not in visited:
                    dfs(neigh)
            
        
        n, visited = len(isConnected), set()
        Graph =[[] for _ in range(n)]

        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    Graph[i].append(j)
                    Graph[j].append(i)
        
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count