# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        result = []
        def collect(s):
            if len(s) == n:
                result.append(s)
                return
            
            if not s or s[-1] == "1":
                collect(s+"0")
                collect(s+"1")
            else:
                collect(s+"1")
        collect("")
        return result