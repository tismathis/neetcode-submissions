class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0 


        if len(nums) == 1 : 
            return nums[0] 

        maxValue = 0 

        def multiply (i,j,nums) : 
            value = 0
            for i in range(i,j+1) :
                value *=nums[i] 
            return value 

        i = 0
        j = 0

        while j < len(nums) - 1 : 
            maxValue = max(maxValue,multiply(i,j))

            if nums[j+1] == 0 :
                j +=2 
                i = j-1  #move the pointers 
            else :
                j +=1
        return maxValue 


        