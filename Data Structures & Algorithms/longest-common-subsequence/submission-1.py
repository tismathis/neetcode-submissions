class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length1 = 0 
        length2 = 0 

        i,j = 0,0

        if len(text1) == 0 or len(text2) == 0 :
            return 0 

        while i < len (text1) and j < len(text2) : 
            if text1[i] == text2[j] :
                i +=1 
                length1 +=1 
            j +=1 
        
        m,n = 0,0

        while m < len (text1) and n < len(text2) : 
            if text1[m] == text2[n] :
                m +=1 
                length2 +=1 
            n +=1 
        return max(length1,length2)
             

