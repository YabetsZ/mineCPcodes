class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        nums = [1]*numOnes
        nums.extend([0]*numZeros)
        nums.extend([-1]*numNegOnes)
        return sum(nums[:k])