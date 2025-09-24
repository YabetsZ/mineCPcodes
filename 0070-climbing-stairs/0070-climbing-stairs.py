class Solution:
    def climbStairs(self, n: int, memo=None) -> int:
        if memo is None:
            memo = {1:1, 2:2}
        
        if n not in memo:
            memo[n] = self.climbStairs(n-1, memo) + self.climbStairs(n-2, memo)
        
        return memo[n]