class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        best = minCurrent = maxCurrent = nums[0] 

        for x in nums[1:] : 
            candidates = (best , minCurrent*x ,maxCurrent*x)

            maxCurrent = max(candidates) 
            minCurrent = min(candidates) 
            best = max(best,maxCurrent)
        return best 