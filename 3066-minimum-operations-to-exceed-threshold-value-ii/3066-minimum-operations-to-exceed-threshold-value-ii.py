class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        counter = 0
        while nums[0] < k:
            x, y = heappop(nums), heappop(nums)
            heappush(nums, 2*min(x, y) + max(x, y))
            counter += 1
        
        return counter