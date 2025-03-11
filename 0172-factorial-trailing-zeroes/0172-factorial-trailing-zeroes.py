class Solution:
    def trailingZeroes(self, n: int) -> int:
        def trailing(num):
            count = 0
            while num % 10 == 0:
                num //= 10
                count += 1
            return count
        def factorial(num):
            if num == 0 or num == 1:
                return 1
            return num * factorial(num-1)
        return trailing(factorial(n))
