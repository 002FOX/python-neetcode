#Straight to the point, two stack solution
class MinStack:
    def __init__(self):
        self.stack = []
        self.mini = float('inf')
        self.minStack = []

    def push(self, val: int) -> None:
        self.mini = min(self.mini, val)
        self.minStack.append(self.mini)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        if len(self.stack) == 0:
            self.mini = float('inf')
        else:
            self.mini = self.minStack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
