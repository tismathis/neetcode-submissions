class Solution:
    def countSubstrings(self, s: str) -> int:
        
        counter = 0 

        if len(s) == 0 : 
            return 0 
        
        if len(s) == 1 : 
            return 1 

        for i in range(len(s)) : 

            counter +=1  
            #if len impair 
            
            j = 1 
            while i-j >= 0 and i+j < len(s) and s[i-j] == s[i+j] : 
                counter +=1 
                j +=1 
            
            
            j = 0
            while i-j >= 0  and i+j+1 < len(s) and s[i-j] == s[i+j+1] :
                counter +=1 
                j +=1 
        return counter 

