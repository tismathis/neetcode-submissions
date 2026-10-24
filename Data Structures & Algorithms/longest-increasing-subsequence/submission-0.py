class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        length = 0 

        visited = set() 

        l,r = 0,len(nums) -1 

        #base case : 

        if len(nums) == 0 : 
            return 0 

        while l < r : 
            if nums[l] in visited : 
                l +=1 
            if nums[r] in visited : 
                r -=1 
            if nums[l] > nums [r] : 
                visited.add(nums[l])
                l +=1 
            else : 
                visited.add(nums[r]) 
                r -=1 
                length +=1 
        return length  




