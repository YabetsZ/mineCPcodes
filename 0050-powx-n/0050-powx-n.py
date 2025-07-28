class Solution:
    def myPow(self, x: float, n: int) -> float:
        result, reverse = 1, n < 0
        n = abs(n)
        while n > 0:
            if n & 1 > 0:
                result *= x
            x *= x
            n >>= 1
        
        return result if not reverse else 1.0/result