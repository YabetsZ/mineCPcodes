class Solution:
    def smallestNumber(self, pattern: str) -> str:
        self.pat = pattern
        picked = [0]*10
        def generate(s, start, end):
            result = None
            for i in range(start, end):
                if picked[i] == 0:
                    picked[i] += 1
                    s.append(str(i))
                    if len(s) == len(self.pat)+1:
                        return s
                    
                    if self.pat[len(s)-1] == "I":
                        result = generate(s, i+1, 10)
                    else:
                        result = generate(s, 1, i)
                    
                    if result:
                        return result
                    s.pop()
                    picked[i] -= 1
        return "".join(generate([], 1, 10))
                
