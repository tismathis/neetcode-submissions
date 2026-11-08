class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        temp = [0] * len(temperatures)

        n = len(temperatures)

        for i in range(len(temperatures)) : 

            currTemp = temperatures[i] 
            j = i+1 
            counter = 0 
            while j < n and temperatures[j] <= temperatures[i] : 
                j +=1 
            if j < n :
                temp[i] = j-i 

        return temp 
                
