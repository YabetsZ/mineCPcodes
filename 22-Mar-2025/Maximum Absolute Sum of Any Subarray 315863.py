# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_= min_count= max_= max_count= 0
        for num in nums:
            # handle min
            min_count += num
            if min_count > 0:
                min_count = 0
            min_ = min(min_, min_count)
            # handle max
            max_count += num
            if max_count < 0:
                max_count = 0
            max_ = max(max_, max_count)
        return max_ if max_ > abs(min_) else abs(min_)
            