class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length = 0 

        i,j = 0,0

        if len(text1) == 0 or len(text2) == 0 :
            return 0 

        while i < len (text1) and j < len(text2) : 
            if text1[i] == text2[j] :
                i +=1 
                length +=1 
            j +=1 
        return length
             

