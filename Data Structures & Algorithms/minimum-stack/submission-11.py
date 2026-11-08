class MinStack:

    def __init__(self):
        self.stack = {}
        

    def push(self, val: int) -> None:
        self.stack[len(self.stack)] = val 
        

    def pop(self) -> None:
        del self.stack[len(self.stack) - 1]
        

    def top(self) -> int:
        return self.stack.get(len(self.stack)-1)
        

    def getMin(self) -> int:
        minVal = self.stack[0] 

        for i in self.stack.values() : 
            if i < minVal : 
                minVal = i 
        return minVal 

        
