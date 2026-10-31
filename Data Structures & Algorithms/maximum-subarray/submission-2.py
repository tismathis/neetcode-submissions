class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 0 : 
            return 0 
        
        if len(nums) == 1 :
            return nums[0]

        
        def split(res,i) :
            if i == len(nums)-1 :
                return res

            return max(split(res+nums[i],i+1),split(res,i+1)) 

        res = 0

        return split(res,0)

