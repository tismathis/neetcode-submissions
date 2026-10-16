class Solution:
    def rob(self, nums: List[int]) -> int:
        

        def search(i) : 
            counter = 0 
            while i < len(nums)-2 : 
                if nums[i] + nums[i+2] > nums [i+1] : 
                    counter +=nums[i] 
                    search(i+2)
                else : 
                    search(i+1) 
            return counter 
        
        return search(0)

                


