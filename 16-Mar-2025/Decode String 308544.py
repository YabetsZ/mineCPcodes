# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        def decode(s):
            bracket = []
            result = string = num = ""
            
            i = 0
            while i < len(s):
                char = s[i]
                if char.isdigit():
                    num += char
                elif char == "[":
                    bracket.append(char)
                    while bracket:
                        i += 1
                        if s[i] == "[":
                            bracket.append(s[i])
                        elif s[i] == "]":
                            bracket.pop()
                        if bracket:
                            string += s[i]
                        # print(string, "char", i)
                    result += int(num) * decode(string)
                    num = string = ""
                else:
                    result += char
                i += 1
            return result 
        return decode(s)  
