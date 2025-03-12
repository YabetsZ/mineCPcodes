# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        nonLegit = -1
        legitMax = -1
        legitMin = -1
        count = 0

        for i in range(len(nums)):
            num = nums[i]
            if num < minK or num > maxK: nonLegit = i
            if num == minK: legitMin = i
            if num == maxK: legitMax = i

            left = min(legitMax, legitMin)
            if nonLegit < left:
                count += left - nonLegit
        return count
            
