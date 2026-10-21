class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s[0] == "0" or not s : 
            return 0 



        prev1 ,prev2 = 1,1 #combin pssible aux etpes prec :

        for i in range(2,len(s)) : 
            current = 1 

            if s[i-1] !="0" : 
                current +=prev1 
                if 10 < int(s[i-2:i]) <27 : 
                    current +=prev2 
            prev2,prev1 = prev1,current 
        return prev1
        