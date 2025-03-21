class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def permutation(added, arr):
            if len(arr) == len(nums):
                result.append(arr[:])
            for i in range(len(nums)):
                if i not in added:
                    arr.append(nums[i])
                    added.add(i)
                    permutation(added, arr)
                    arr.pop()
                    added.discard(i)
        permutation(set(), [])
        return result