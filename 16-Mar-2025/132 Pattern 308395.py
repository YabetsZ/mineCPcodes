# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        one = 0 # it's an index
        prev_min = [float("inf")]
        stack = []
        for i in range(1, len(nums)):
            prev_min.append(one)
            if nums[one] > nums[i]:
                one = i

            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if stack:
                idx = stack[-1]
                if idx != 0 and nums[i] > nums[prev_min[idx]]:
                    return True
            stack.append(i)
        return False
                