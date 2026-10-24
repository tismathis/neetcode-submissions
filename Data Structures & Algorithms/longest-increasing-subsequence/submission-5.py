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
                continue 
            if nums[r] in visited : 
                r -=1 
                continue 
            if nums[l] > nums [r] : 
                visited.add(nums[l])
                l +=1 
            else : 
                if visited and nums[r] > max(visited) : 
                    length -=1 
                visited.add(nums[r]) 
                r -=1 
                length +=1 
        return length  




