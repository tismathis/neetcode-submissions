class Solution:
    def numDecodings(self, s: str) -> int:
        

        if s[0] == "0" : 
            return 0 
        
        i = 1 

        counter = 0  

        while i < len(s) : 
            if 0 < int(s[i]) < 10 and 0 < int(s[i-1]) < 10 : 
                counter +=1
                if 0 < int(s[i]) < 3 and 0 < int(s[i-1]) < 7 : 
                    counter +=1  
                i +=2  
            else :
                return 0 
        return counter 

        