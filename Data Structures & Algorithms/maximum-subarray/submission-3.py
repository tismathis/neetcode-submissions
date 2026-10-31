class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = best = nums[0]
        for x in nums[1:]:
            cur = max(x, cur + x)   # extend the previous subarray, or start new at x
            best = max(best, cur)
        return best