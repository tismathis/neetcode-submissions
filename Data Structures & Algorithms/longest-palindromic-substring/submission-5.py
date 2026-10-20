class Solution:
    def longestPalindrome(self, s: str) -> str:
        
    

        if len(s) == 0 :
            return ""
        
        if len(s) == 1 : 
            return s[0]

        maxLength = 0
        word = "" 

        for i in range(len(s)) : 
            
            currentLength = 0 
            j = 1 
            while i-j >= 0 and i+j < len(s) and s[i-j] == s[i+j] : 
                currentLength +=2
                if currentLength > maxLength : 
                    word =s[i-j:i+j+1]
                    maxLength = currentLength
                j +=1 
            continue 
        return word
        

            

        


