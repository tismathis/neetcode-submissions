class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        if len(temperatures) == 0:
            return None 

        stack = [0]  

        finalTab = [0] * len(temperatures) 


        for i in range (1,len(temperatures)) : 
            while stack and temperatures[i] > temperatures[stack[-1]] : 
                prev = stack.pop() 
                finalTab[prev] = i-prev
            stack.append(i) 
        return finaltab



            

