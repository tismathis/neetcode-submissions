class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        

        def helper(strr) : 

            m = len(s) // 2 #if impair good 
            
            if s[0,m] == s[-1,m] : 
                return s[0,m] + s[-1,m] 
            return helper(m//2)

        return helper(s)
        
        


