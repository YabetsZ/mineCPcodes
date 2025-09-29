class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        def dp(i, memo=None):
            if memo is None:
                memo = {}
            if i >= len(s):
                return True 
            if i in memo:
                return memo[i]

            st = ""
            for (idx, ch) in enumerate(s[i:]):
                st += ch
                if st in wordSet:
                    memo[i+idx+1] = dp(i + idx+1, memo)
                    if memo[i+idx+1]:
                        return True
            memo[i] = False 
            return False
        return dp(0)
