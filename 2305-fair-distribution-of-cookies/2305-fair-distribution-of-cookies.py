class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        child = [0]*k
        def backtrack(i, minOfMax): # i is the current cookies index
            if i == len(cookies):
                return min(minOfMax, max(child))
            if max(child) >= minOfMax:
                return minOfMax
            for idx in range(k):
                child[idx] += cookies[i]
                minOfMax = backtrack(i+1, minOfMax)
                child[idx] -= cookies[i]
            return minOfMax
        
        return backtrack(0, float('inf'))

