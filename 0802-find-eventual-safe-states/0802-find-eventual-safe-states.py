class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # I don't know which one to use khan's or dfs. let's go with dfs
        # WHITE, GRAY, BLACK = 0, 1, 2
        Colors = [0] * len(graph)
        ans = []
        def dfs(node):
            if Colors[node] == 2:
                return True
            elif Colors[node] == 1:
                return False

            Colors[node] = 1
            result = True

            for neigh in graph[node]:
                result = dfs(neigh) and result
                    
            if result:
                Colors[node] = 2
                ans.append(node)

            return result
        for node in range(len(graph)):
            if Colors[node] == 0:
                dfs(node)
        ans.sort()
        return ans
