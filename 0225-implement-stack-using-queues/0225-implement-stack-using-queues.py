from collections import deque

class MyStack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        popped_value = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return popped_value

    def top(self) -> int:
        top_value = self.pop()
        self.push(top_value)
        return top_value

    def empty(self) -> bool:
        return not self.queue1
