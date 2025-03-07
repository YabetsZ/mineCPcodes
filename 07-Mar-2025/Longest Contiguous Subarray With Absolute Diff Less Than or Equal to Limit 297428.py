# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        min_dq = deque()
        max_dq = deque()
        ans = 0
        left = 0
        for right in range(n):
            while min_dq and nums[min_dq[-1]] > nums[right]:
                min_dq.pop()
            while max_dq and nums[max_dq[-1]] < nums[right]:
                max_dq.pop()
            min_dq.append(right)
            max_dq.append(right)

            while nums[max_dq[0]] - nums[min_dq[0]] > limit:
                if max_dq[0] > min_dq[0]:
                    left = min_dq[0] + 1
                    min_dq.popleft()
                else:
                    left = max_dq[0] + 1
                    max_dq.popleft()
            
            ans = max(ans, right - left + 1)
        return ans