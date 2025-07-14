class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_pair = -float("inf")
        left, right = 0, len(nums)-1
        while left < right:
            max_pair = max(max_pair, nums[left]+nums[right])
            left += 1
            right -= 1
        
        return max_pair