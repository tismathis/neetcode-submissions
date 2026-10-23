class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        for i in range(len(s)) : 

            substring += s[i]  

            for word in wordDict : 
                if substring == word : 
                    wordbreak(s[len(substring),],wordDict)
                else : 
                    continue 
        if len(substring) == 0:
            return True 
        return False 


        