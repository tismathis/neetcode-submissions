class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def sum(i) :
            counter = 0 
            for pile in piles : 
                counter += Math.floor(pile/i)
            return counter

        l,r =1,max(piles)


        while l <= r : 

            m = l + (r-l)//2 

            if sum(m) > h : #we are in the case where we are taking too much time so we need to re-iterate 
                r = m - 1 
            
            elif sum(m) < h :
                l = m + 1 
        return sum(m)



        