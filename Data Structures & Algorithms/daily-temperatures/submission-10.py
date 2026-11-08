class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        if len(temperatures) == 0:
            return None 

        stack = [temperatures[0]]  

        finalTab = []


        for i in range (1,len(temperatures)) : 
            if temperatures[i] > stack[-1] : 
                stack.append(temperatures[i]) 
            else : 
                for j in range (i) : 
                    finalTab.append(i-j)  
                    stack.pop()
        return finalTab



            

