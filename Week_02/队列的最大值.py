class MaxQueue:

    def __init__(self):
        self.queue = []
        self.deque = []
    def max_value(self) -> int:
        if len(self.deque) != 0:
            return self.deque[0]

    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1]<value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.append(value)
    def pop_front(self) -> int:
        result = self.queue.pop(0)
        if result == self.deque[0]:
            self.deque.pop(0)
        return result

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()