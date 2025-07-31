class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)

        @lru_cache(None)
        def dfs(idx):
            pt, bp = questions[idx]
            if idx + bp + 1 > n - 1:
                return pt
            
            result = 0
            for i in range(idx + bp + 1, n):
                result = max(result, dfs(i))
                
            return pt + result
        
        result = 0
        for i in range(n):
            result = max(result, dfs(i))
        
        return result
