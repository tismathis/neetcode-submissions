class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        while i < len(nums) : 
            i +=nums[i]
        return i == len(nums)-1
           