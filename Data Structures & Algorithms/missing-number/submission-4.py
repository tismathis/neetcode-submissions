class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        visited = set(nums)
        for i in range(0,len(nums)) : 
            if i not in visited : 
                return i 
            
