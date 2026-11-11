
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def hours_needed(i) :
            counter = 0 
            for pile in piles : 
                counter += (pile + i - 1) // i
            return counter

        l,r =1,max(piles)


        while l <= r : 

            m = l + (r-l)//2 

            hours = hours_needed(m)
            if hours == h : 
                return m

            elif hours > h : #we are in the case where we are taking too much time so we need to re-iterate 
                r = m -1
            
            else :  #we found a valid number but we still need to check if there is a better solution 
                l = m + 1 
        



        