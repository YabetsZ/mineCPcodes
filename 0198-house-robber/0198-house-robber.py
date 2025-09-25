class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            if i == 0:
                return nums[i]
            elif i == 1:
                return max(nums[i-1], nums[i])
            
            return max(dp(i-2)+nums[i], dp(i-1))
        
        return dp(len(nums)-1)