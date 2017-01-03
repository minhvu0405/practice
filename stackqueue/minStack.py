class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
    # @param x, an integer
    def push(self, x):
        self.stack.append(x)
        if len(self.stack) == 1 or x < self.minStack[-1]:
            self.minStack.append(x)

    # @return nothing
    def pop(self):
        if self.stack:
            x = self.stack.pop()
            if x == self.minStack[-1]:
                self.minStack.pop()
 
    # @return an integer
    def top(self):
        if self.stack:
            return self.stack[-1]
        return -1

    # @return an integer
    def getMin(self):
        if self.minStack:
            return self.minStack[-1]
        return -1