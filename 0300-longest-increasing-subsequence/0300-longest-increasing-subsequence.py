class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result_arr = [0]*len(nums)
        for i in range(len(nums)):
            num = nums[i]
            for j in range(0, i):
                if nums[j] < num and result_arr[j] + 1 > result_arr[i]:
                    result_arr[i] = result_arr[j] + 1
            if result_arr[i] == 0:
                result_arr[i] = 1
    
        return max(result_arr)