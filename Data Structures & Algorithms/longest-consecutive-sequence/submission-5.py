class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        longest = 1
        compteur = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue  # duplicate, skip without breaking the streak
            elif nums[i] - nums[i - 1] == 1:
                compteur += 1
                longest = max(longest, compteur)
            else:
                compteur = 1  # streak broken, restart at this number

        return longest