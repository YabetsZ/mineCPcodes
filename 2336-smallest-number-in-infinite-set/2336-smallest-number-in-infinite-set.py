class SmallestInfiniteSet:

    def __init__(self):
        self.set = set()
        self.heap = []
        self.count = 1

    def popSmallest(self) -> int:
        if not self.set:
            self.count += 1
            return self.count - 1
        else:
            num = heappop(self.heap)
            self.set.discard(num)
            return num

    def addBack(self, num: int) -> None:
        if num < self.count and num not in self.set:
            heappush(self.heap, num)
            self.set.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)