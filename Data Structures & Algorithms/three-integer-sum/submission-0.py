class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set(nums)
        res = []
        nums = nums.sorted()
        i = 0
        j = len(nums) -1 

        while i < j : 
            doubleP = nums[i] + nums [j]
            complement = -doubleP
            
            if complement in s :
                res1 = [nums[i],nums[j],complement]
                res.append(res1)
                
            else : 
                if doubleP > 0 :
                    j -=1
                else :
                    i +=1 
            i +=1
            j -=1

