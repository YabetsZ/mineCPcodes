class MyStack:

    def __init__(self):
        self.main = deque()
        self.peek = None

    def push(self, x: int) -> None:
        self.main.append(x)
        self.peek = x

    def pop(self) -> int:
        for i in range(len(self.main)-1):
            num = self.main.popleft()
            if i == len(self.main) - 2:
                self.peek = num
            self.main.append(num)
        if len(self.main) == 1:
            self.peek = None
        return self.main.popleft()
    

    def top(self) -> int:
        return self.peek

    def empty(self) -> bool:
        return len(self.main) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()