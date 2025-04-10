"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, empl: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        def dfs(node):
            if not graph[node].subordinates:
                return graph[node].importance
            count = graph[node].importance
            for sub in graph[node].subordinates:
                count += dfs(sub)
            return count
        for data in empl:
            graph[data.id] = data
        return dfs(id)