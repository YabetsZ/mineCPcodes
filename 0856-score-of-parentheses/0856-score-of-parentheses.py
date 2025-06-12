class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        for sign in s:
            if sign == "(":
                if stack:
                    stack[-1] = 2
                    stack.append(1)
                else:
                    stack.append(1)
            else:
                if stack.pop() == 1:
                    ans += 1
                else:
                    ans *= 2
        return ans


                