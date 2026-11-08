class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        if len(temperatures) == 0:
            return None 

        stack = [0]  

        finalTab = [0] * len(temperatures) 


        for i in range (1,len(temperatures)) : 
            if temperatures[i] >= temperatures[stack[-1]] : 
                stack.append(i) 
            else : 
                for j in range (i) : 
                    finalTab[j] = i-j   
                    stack.pop()
        return finalTab



            

