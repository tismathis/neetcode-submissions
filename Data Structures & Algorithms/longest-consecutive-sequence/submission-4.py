class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #possible to this with a heap ? 
        max = 0
        res = nums.sort()
        i = 0
        while i < len(nums)-2 :
            compteur = 0
            while (nums[i+1] - nums[i] == 1) :
                compteur +=1
                i+=1
                if compteur > max :
                    max = compteur
            else :
                i +=1
        return max
            
            
            