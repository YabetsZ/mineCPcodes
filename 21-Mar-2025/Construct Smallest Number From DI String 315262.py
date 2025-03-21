# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        self.pat = pattern
        picked = set()
        def generate(s, start, end):
            
            for i in range(start, end):
                if i not in picked:
                    picked.add(i)
                    s.append(str(i))
                    if len(s) == len(self.pat)+1:
                        return s
                        
                    result = None
                    if self.pat[len(s)-1] == "I":
                        result = generate(s, i+1, 10)
                    else:
                        result = generate(s, 1, i)
                    
                    if result:
                        return result
                    s.pop()
                    picked.discard(i)
        return "".join(generate([], 1, 10))
                
