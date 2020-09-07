class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.min_stack) == 0 or self.stack[self.min_stack[-1]]>x:
            self.min_stack.append(len(self.stack)-1)



    def pop(self) -> None:
        if not self.min_stack:
            raise Exception("栈为空")
        t = self.stack.pop()
        if len(self.stack) == self.min_stack[-1]:
            self.min_stack.pop()
        return t


    def top(self) -> int:
        if not self.min_stack:
            raise Exception("栈为空")
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.min_stack:
            raise Exception("栈为空")
        return self.stack[self.min_stack[-1]]