class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        if m == 0 or n == 0 : 
            return 0 
        

        def recursion(i,j) : 

            result = 0
            if i == 0 and j == 0 : 
                return 1 

            if  not (0 <= i <= m and 0 <= j <= n) : 
                return 0 
            else : 
                result +=recursion(i-1,j) #up
                result +=recursion(i,j-1) # left 
            return result 
        
        return recursion(m-1,n-1) 

