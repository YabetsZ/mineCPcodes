class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        result = 1
        left = 0
        accumulator = 0
        for right in range(len(nums)):
            while accumulator & nums[right] != 0 and left != right:
                accumulator ^= nums[left]
                left += 1
            accumulator |= nums[right]
            result = max(result, right-left+1)
        
        return result