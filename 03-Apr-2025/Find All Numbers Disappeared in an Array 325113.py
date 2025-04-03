# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = set()
        i = 0
        while i < len(nums):
            cor = nums[i]-1 # correct
            if nums[cor] != nums[i]:
                if nums[i] in result:
                    result.discard(nums[i])
                nums[cor], nums[i] = nums[i], nums[cor]
            else:
                if cor != i:
                    result.add(i+1)
                i += 1
        result = list(result)
        return result
                
                
        