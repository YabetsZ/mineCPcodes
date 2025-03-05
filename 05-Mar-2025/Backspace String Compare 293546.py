# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def clean(word):
            stack = []
            for letter in word:
                if letter == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(letter)
            return "".join(stack)
            
        return clean(s) == clean(t)
        