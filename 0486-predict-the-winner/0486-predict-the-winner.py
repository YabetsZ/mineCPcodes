class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # try to search for every possible solution
        def search(left, right):
            if left == right:
                return nums[left]
            return max(nums[left] - search(left+1, right), nums[right] - search(left, right-1))
        
        return search(0, len(nums)-1) >= 0 # since player one starts first! wooow!

