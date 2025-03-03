class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_ = 1
        n = len(nums)
        for i, num in enumerate(nums):
            max_ -= 1
            max_ = max(max_, num)
            if max_ <= 0 and i < n-1:
                return False
        return True
