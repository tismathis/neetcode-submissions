class Solution:
    def isValid(self, s: str) -> bool:
        
        i = 0
        j = len(s)

        if len(s) % 2 !=0 :
            return False

        while i < j : 
            if s[i] == "{" and s[j] == "}":
                i+=1
                j-=1
            elif s[i] == "(" and s[j] == ")":
                i+=1
                j-=1
            elif s[i] == "[" and s[j] == "]":
                i+=1
                j-=1
            else :
                return False
        return True
                