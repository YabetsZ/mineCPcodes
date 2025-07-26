class Solution:
    def fib(self, n: int, lookUp=None) -> int:
        lookUp = {} if lookUp is None else lookUp
        if n in lookUp:
            return lookUp[n]
        if n < 2:
            return n
        
        lookUp[n] = self.fib(n-1, lookUp) + self.fib(n-2, lookUp)
        return lookUp[n]