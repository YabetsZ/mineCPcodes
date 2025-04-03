# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = set()
        i = 0
        while i < len(nums):
            correct = nums[i]-1
            if nums[correct] != nums[i]:
                nums[correct], nums[i] = nums[i], nums[correct]
            else:
                if i != correct:
                    result.add(nums[i])
                i += 1
        return list(result)

