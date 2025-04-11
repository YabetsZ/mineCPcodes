class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(i):
            if not Tree[i]:
                return 0
            print(i)
            result = float("-inf")
            for child in Tree[i]:
                result = max(result, dfs(child))
            return result + informTime[i]
        
        Tree = [[] for _ in range(n)]
        head = None
        for v in range(len(manager)):
            u = manager[v] # u -> v
            if u == -1:
                head = v
            else:
                Tree[u].append(v)
        return dfs(head)
        
        