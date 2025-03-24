# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        left, right = 0, len(nums)-1
        result = [-1, -1]
        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
        
                right = mid - 1
                result[0] = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[right] > target:
                right = mid - 1
        left, right = 0, len(nums)-1
        if result[0] != -1:
            while left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    left = mid + 1
                    result[1] = mid
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[right] > target:
                    right = mid - 1
        return result