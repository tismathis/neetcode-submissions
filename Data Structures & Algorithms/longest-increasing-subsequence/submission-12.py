class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * int(len(nums)-1)

        for i in range(1,len(nums)-1) : 
            prev,curr = i-1 , i 
            if nums[curr] > nums[prev] : 
                dp[curr] = dp[prev] + 1 
            curr,prev = curr + 1,curr 
        return dp[len(nums)-1]
           




        