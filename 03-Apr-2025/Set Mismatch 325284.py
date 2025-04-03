# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # using cyclic sort
        i = 0
        while i < len(nums):
            cor = nums[i]-1
            if nums[cor] != nums[i]:
                nums[cor], nums[i] = nums[i], nums[cor]
            else:
                i += 1
        for i in range(1, len(nums)+1):
            if i != nums[i-1]:
                return [nums[i-1], i]
        