class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        temp = [0] * len(temperatures)

        for i in range(len(temperatures)) : 

            currTemp = temperatures[i] 
            j = i+1 
            counter = 0 
            while currTemp < temperatures[j-1] : 
                counter +=1 
                j +=1 
            temp[i] = counter 

        return temp 
                
