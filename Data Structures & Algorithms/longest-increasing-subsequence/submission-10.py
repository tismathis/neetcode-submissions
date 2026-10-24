class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * int(len(nums)-1)

        for i in range(1,len(nums)-1) : 
            if nums[i] > nums[i-1] : 
                dp[i] = dp[i-1] + 1 
        return dp[int(len(nums)-1)]  


        