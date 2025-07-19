class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def GCF(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        count = Counter(deck)
        result = 0
        for a in count.values():
            result = GCF(result, a)

        return True if result > 1 else False
