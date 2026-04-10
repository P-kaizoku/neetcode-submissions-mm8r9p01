class MinStack:

    def __init__(self):
        self.stack = []
        self.mStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mStack:
            top = self.mStack[-1]
            if top > val:
                self.mStack.append(val)
            else:
                self.mStack.append(top)
        else:
            self.mStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.mStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        return self.mStack[-1]

    def getMin(self) -> int:
        return self.mStack[-1]
