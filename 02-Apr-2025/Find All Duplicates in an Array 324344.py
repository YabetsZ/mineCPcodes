# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        set_ = set()
        result = []
        for i in range(len(nums)):
            if nums[i] in set_:
                result.append(nums[i])
            else:
                set_.add(nums[i])
        
        return result
        