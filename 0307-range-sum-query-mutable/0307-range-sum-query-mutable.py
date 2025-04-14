class NumArray:
    def __init__(self, nums: List[int]):
        self.nums, n = [0] + nums, len(nums)
        for i in range(1, n+1):
            p = i + (i & -i) # immediate_next
            if p <= n:
                self.nums[p] += self.nums[i]
    def update(self, index: int, val: int) -> None:
        index += 1
        diff = val - self.sumRange(index-1, index-1)
        while index < len(self.nums):
            self.nums[index] += diff
            index += index & -index
    def sum(self, index):
        result = 0
        while index > 0:
            result += self.nums[index]
            index -= index & -index
        return result
    def sumRange(self, left: int, right: int) -> int:
        return self.sum(right+1) - self.sum(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)