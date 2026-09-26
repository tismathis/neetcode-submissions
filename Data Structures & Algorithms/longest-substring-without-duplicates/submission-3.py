class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max = 0

        i = 0 
        j = 1 
        index = 1
        counter = 0 

        while j < len(s)-1 : 
            

            if ord(s[j]) == ord(s[i])+index :
                counter +=1
                index +=1
                if counter > max :
                    max = counter
            else :
                i=j
                index = 0;
                counter = 0
            j +=1
        return max

        