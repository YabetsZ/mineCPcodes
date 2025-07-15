class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack, set_ = [], set()
        for char in s:
            while stack and count[stack[-1]] > 1 and char not in set_ and stack[-1] > char:
                popped = stack.pop()
                count[popped] -= 1
                set_.discard(popped)

            if char not in set_:
                stack.append(char)
                set_.add(char)

        return "".join(stack)