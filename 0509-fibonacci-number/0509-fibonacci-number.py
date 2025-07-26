class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        tab = [0, 1]
        
        for _ in range(2, n+1):
            tab[0], tab[1] = tab[1], tab[0]
            tab[1] = tab[0] + tab[-1]

        return tab[-1]