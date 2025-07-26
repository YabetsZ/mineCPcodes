class Solution:
    def fib(self, n: int) -> int:
        tab = deque([0, 1])
        
        for _ in range(2, n+1):
            cur = tab[0] + tab[-1]
            tab.popleft()
            tab.append(cur)
            
        return tab[-1]