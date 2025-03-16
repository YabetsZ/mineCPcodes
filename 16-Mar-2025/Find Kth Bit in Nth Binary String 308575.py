# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def findIn(s):
            if len(s) >= k:
                return s[k-1]
            processed = "".join("1" if c == "0" else "0" for c in s)[::-1]
            return findIn("".join([s, "1", processed]))
        return findIn("0")