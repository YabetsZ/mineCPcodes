class BIT:
    def __init__(self, arg):
        if isinstance(arg, int):
            self.n = arg
            self.tree = [0] * (self.n + 1)
        else:
            arr = arg
            self.n = len(arr) - 1
            self.tree = [0] + arr[1:]
            for i in range(1, self.n + 1):
                j = i + (i & -i)
                if j <= self.n:
                    self.tree[j] += self.tree[i]

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    def range_query(self, l, r):
        return self.query(r) - self.query(l - 1)

class Solution:
    def createSortedArray(self, nums: List[int]) -> int:
        bit = BIT(10**5)
        result = 0
        for i in range(len(nums)):
            result += min(bit.query(nums[i]-1), bit.range_query(nums[i]+1, 10**5))
            bit.update(nums[i], 1)
        
        return result
