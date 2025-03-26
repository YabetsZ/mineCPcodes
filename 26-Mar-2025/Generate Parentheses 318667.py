# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []
        def generate(s):
            if len(s) == 2*n:
                if stack:
                    return
                result.append(s)
                return
            if stack:
                stack.pop()
                generate(s+")")
                stack.append("(")
            stack.append("(")
            generate(s+"(")
            stack.pop()
        generate("")
        return result