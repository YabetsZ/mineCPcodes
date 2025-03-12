# Problem: Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:
    def __init__(self):
        self.main = deque()
        self.peek = None

    def push(self, x: int) -> None:
        self.main.append(x)
        self.peek = x

    def pop(self) -> int:
        for i in range(len(self.main)-1):
            if i == len(self.main) - 2:
                self.peek = self.main[0]
            self.main.append(self.main.popleft())
        return self.main.popleft()
    

    def top(self) -> int:
        return self.peek

    def empty(self) -> bool:
        return len(self.main) == 0