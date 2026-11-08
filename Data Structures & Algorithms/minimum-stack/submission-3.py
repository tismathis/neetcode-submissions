class MinStack:

    def __init__(self):
        self.stack = {}
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack[len(stack)-1] = "a"
        

    def top(self) -> int:
        self.stack[len(stack)-1]
        

    def getMin(self) -> int:
        minVal = self.stack[0] 

        for i in self.stack.values : 
            if i < minVal : 
                minVal = i 
        return minVal 

        
