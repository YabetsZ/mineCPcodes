
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ans = ""
        count = Counter(s)
        ans += "1"*(count["1"]-1) if count["1"] > 0 else ""
        ans += "0"*count["0"]
        ans += "1" if count["1"] > 0 else ""
        return ans

