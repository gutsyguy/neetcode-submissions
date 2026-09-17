class MinStack:
    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        min_val = self.getMin()
        print(min_val)
        if min_val is None or val < min_val:
            min_val = val
        
        self.stack.append([val, min_val])

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        
