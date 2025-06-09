class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        for i in range(len(nums)):
            if i < k:
                heappush(self.heap, nums[i])
            else:
                heappushpop(self.heap, nums[i])

    def add(self, val: int) -> int:
        heappushpop(self.heap, val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)