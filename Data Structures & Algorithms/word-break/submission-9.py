class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        if s == "":
                return True 

        substring = "" 
        for i in range(len(s)) : 

            substring += s[i]  

            for word in wordDict : 
                if substring == word : 
                    if self.wordBreak(s[len(substring):],wordDict) : 
                        return True 
                else : 
                    continue 
        return False 


        