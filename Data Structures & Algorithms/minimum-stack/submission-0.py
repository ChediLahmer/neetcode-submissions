class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []
        
        

    def push(self, val: int) -> None:
        if not self.minimum:
            self.minimum.append(val)
        elif self.minimum[-1] > val:
            self.minimum.append(val)
        else:
            self.minimum.append(self.minimum[-1])
            
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]