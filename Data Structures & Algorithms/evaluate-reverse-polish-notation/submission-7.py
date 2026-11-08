class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        i = 0 

        characters = {"+" : "+" , "-" : "-" , "*" : "* ", "/" : "/"} 

        while i < len(tokens)-1 : 

            if tokens[i] not in characters.keys() : 
                stack.append(tokens[i])
                
            else : 
                if t == "+":
                    res = a + b
                elif t == "-":
                    res = a - b
                elif t == "*":
                    res = a * b
                else:  # "/"
                    res = int(a / b)
                stack.pop()
                stack.pop()
                stack.pop() 
                stack.append(res) 
            i +=1 
        return stack[0] 