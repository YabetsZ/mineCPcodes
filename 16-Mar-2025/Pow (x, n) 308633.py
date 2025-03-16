# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def exp(x, n):
            if n == 0:
                return 1.0
            half = exp(x, n//2)
            if n % 2:
                return half * half * x
            else:
                return half * half
        result = exp(x, abs(n))
        return result if n >= 0 else 1/result