class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        prev_min = [float("inf")]
        next_smaller = [-1] * len(nums)

        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                idx = stack.pop()
                next_smaller[idx] = i
            prev_min.append(min(prev_min[-1], nums[i]))
            stack.append(i)
        print(prev_min, next_smaller)
        for i in range(len(nums)):
            if next_smaller[i] != -1 and prev_min[i] < nums[next_smaller[i]] < nums[i]:
                return True
        return False

