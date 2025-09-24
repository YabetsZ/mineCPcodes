class Solution:
    def fib(self, n: int, memo=None) -> int:
        if memo is None:
            memo = {0: 0, 1: 1}
        
        if n not in memo:
            memo[n] = self.fib(n-1, memo) + self.fib(n-2, memo)
        
        return memo[n]

