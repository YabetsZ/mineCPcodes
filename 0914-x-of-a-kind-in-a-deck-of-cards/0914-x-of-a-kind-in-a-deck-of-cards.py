class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def GCF(a, b):
            if b == 0:
                return a
            if a % b == 0:
                return b
            elif b % a == 0:
                return a
            return GCF(b, a%b)
        count = Counter(deck)
        result = 0
        for a in count.values():
            result = GCF(result, a)

        return True if result > 1 else False
