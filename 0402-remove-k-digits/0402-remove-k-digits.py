class Solution:
    def removeKdigits(self, strNum: str, k: int) -> str:
        stack = []
        count = 0

        for num in strNum:
            while stack and count < k and int(stack[-1]) > int(num):
                stack.pop()
                count += 1
            stack.append(num)
        
        if count != k:
            stack = stack[:-(k-count)]
        if not stack:
            stack.append("0")
        
        return str(int("".join(stack)))
        
        
        return result