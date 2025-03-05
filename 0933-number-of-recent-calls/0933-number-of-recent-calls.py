class RecentCounter:

    def __init__(self):
        self.arr = []

    def ping(self, t: int) -> int:
        self.arr.append(t)
        bottom = t - 3000
        count = 0
        for num in self.arr:
            if num < bottom:
                count += 1
            else:
                break
        return len(self.arr) - count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)