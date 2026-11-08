class MinStack:

    def __init__(self):
        self.stack = {}
        

    def push(self, val: int) -> None:
        self.stack[len(self.stack)] = val 
        

    def pop(self) -> None:
        self.stack[len(self.stack)-1] = None
        

    def top(self) -> int:
        self.stack.get(len(stack)-1)
        

    def getMin(self) -> int:
        minVal = self.stack[0] 

        for i in self.stack.values() : 
            if i < minVal : 
                minVal = i 
        return minVal 

        
