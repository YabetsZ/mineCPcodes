# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isdigit() or len(token)>1:
                stack.append(int(token))
            else:
                second = int(stack.pop())
                first = int(stack.pop())
                if token == "*":
                    stack.append(first * second)
                elif token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "/":
                    stack.append(int(first/second))
        return stack[0]