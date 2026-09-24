class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.toLowerCase()

        i = 0 
        j = len(s) -1

        while i < j : 
            if s[i] != s [j] :
                return False
            elif s[i] == " " or s[j] == " ":
                continue
            else : 
                i+=1 
                j-=1
        return True