class MinStack:
    # To get the minimum we have to store the min every point (operation) of the stack
    # Define 2 stacks
    # 1 stack to store the operations, 1 stack to store the minimums
    def __init__(self):
        # initialize first regular stack
        self.stack = []
        # initialize the minimum stack
        self.minStack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        # take the minimum of val and minStack unless it's empty
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
