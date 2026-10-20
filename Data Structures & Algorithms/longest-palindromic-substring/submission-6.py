class Solution:
    def longestPalindrome(self, s: str) -> str:
        
    

        if len(s) == 0 :
            return ""
        
        if len(s) == 1 : 
            return s[0]

        maxLength = 1
        word = s[0]

        for i in range(len(s)) : 
            
            currentLength = 0 
            
            j = 1 
            while i-j >= 0 and i+j < len(s) and s[i-j] == s[i+j] : 
                if 2*j+ 1 > maxLength : 
                    maxLength = 2*j+1
                    word = s[i-j,i+j+1]
                j +=1

            j = 0 

            while i-j >= 0 and i+1+j < len(s) and s[i-j] == s[i+1+j]:
                if 2*j+2  > maxLength : 
                    maxLength = 2*j+2
                    word = s[i-j,i+j+2]
                j+=1
                
        return word
        

            

        


