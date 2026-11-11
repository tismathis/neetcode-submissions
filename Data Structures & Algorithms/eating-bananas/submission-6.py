import math        # then math.ceil(pile / i)
from math import ceil   # then ceil(pile / i)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def hours_needed(i) :
            counter = 0 
            for pile in piles : 
                counter += math.ceil(pile/i)
            return counter3

        l,r =1,max(piles)


        while l <= r : 

            m = l + (r-l)//2 

            hours = hours_needed(m)
            if hours == h : 
                return hours 

            if hours > h : #we are in the case where we are taking too much time so we need to re-iterate 
                r = m + 1
            
            elif hours < h : #we found a valid number but we still need to check if there is a better solution 
                l = m - 1 
        



        