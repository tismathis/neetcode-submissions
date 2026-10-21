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
            if len(s) % 2 == 1 :
                j = 1 

                while s[i-j] >= 0 and s[i+j] < len(s) and s[i-j] == s[i+j] : 
                    counter +=1 
                    j +=1 
            
            else : 
                j = 0
                while s[i-j] >=0  and s[i+j+1] < len(s) and s[i-j] == s[i+j+1] :
                    counter +=1 
                    j +=1 
        return counter 

