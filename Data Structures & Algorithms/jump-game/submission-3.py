class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums) 

        goal = n-1 

        for i in range(goal,-1,-1) : 
            if nums[i-1] + i-1 == goal :
                goal = i-1 
        return goal == 0
           