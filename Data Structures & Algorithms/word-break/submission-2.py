class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        substring = "" 
        for i in range(len(s)) : 

            substring += s[i]  

            for word in wordDict : 
                if substring == word : 
                    self.wordbreak(s[len(substring),],wordDict)
                else : 
                    continue 
        if len(substring) == 0:
            return True 
        return False 


        