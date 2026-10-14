class Solution:
    def climbStairs(self, n: int) -> int:
        
    

        def recursion(i) :
            if i >= n :
                return i == n
            return recursion(i+1) + recursion(i+2) 

        return recursion(0)
