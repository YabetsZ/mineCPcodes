class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"{": "}", "(": ")", "[": "]"}
        stack = []

        for bracket in s:
            if bracket in ["{", "(", "["]:
                stack.append(pairs[bracket])
            else:
                if not stack or (stack and stack.pop() != bracket):
                    return False
                
        return True if not stack else False
