# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # try to search for every possible solution
        def search(left, right):
            if left == right:
                return nums[left]
            return max(nums[left] - search(left+1, right), nums[right] - search(left, right-1))
        
        return search(0, len(nums)-1) >= 0 

