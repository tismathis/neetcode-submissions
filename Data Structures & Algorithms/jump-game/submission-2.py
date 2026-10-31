class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        i = 0
        while i < len(nums) : 
            i +=nums[i]
        return i == len(nums)-1
           