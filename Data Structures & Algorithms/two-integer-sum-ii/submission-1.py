class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l,r = 0,len(numbers)-1 

        empty = []

        while l < r : 
            if numbers[l] + numbers[r] == target : 
                return [l,r] 

            if numbers[l] + numbers[r] < target : 
                l +=1 
            else : 
                r -=1 
        
            

        
        