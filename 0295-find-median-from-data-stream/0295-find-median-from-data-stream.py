class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if not self.left or num <= -self.left[0]:
            heappush(self.left, -num)
        else:
            heappush(self.right, num)
        self.check()

    def check(self):
        n, m = len(self.right), len(self.left)
        if abs(n - m) > 1:
            drxn = "toLeft" if n > m else "toRight"
            if drxn == 'toLeft':
                popped = heappop(self.right)
                heappush(self.left, -popped)
            else:
                popped = -heappop(self.left)
                heappush(self.right, popped)
        
    def findMedian(self) -> float:
        # print(self.left, self.right)
        n, m = len(self.right), len(self.left)
        if n == m:
            return (-self.left[0]+self.right[0])/2
        elif n > m:
            return self.right[0]
        else:
            return -self.left[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()