class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        result = set()
        for i in range(2**n):
            a = ""
            ptr = 0
            while i > 0:
                if s[ptr].isalpha():
                    if i&1 != 0:
                        a += s[ptr].upper()
                    else:
                        a += s[ptr].lower()
                else:
                    a += s[ptr]
                ptr += 1
                i >>= 1
            a += s[ptr:]
            result.add(a)
        
        return list(result)

            