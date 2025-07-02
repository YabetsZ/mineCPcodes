class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        result = []
        for word in queries:
            temp, j = True, 0
            for i in range(len(word)):
                if j >= len(pattern) or pattern[j] != word[i]:
                    if word[i].islower(): continue
                    else:
                        temp = False
                        break
                else:
                    j += 1
            result.append(temp if j >= len(pattern) else False)
        
        return result