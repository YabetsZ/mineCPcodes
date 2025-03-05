# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temp)
        for i in range(len(temp)):
            while stack and temp[stack[-1]] < temp[i]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result