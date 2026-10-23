class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        substring = "" 
        for i in range(len(s)) : 
            if substring == "":
                return True 
            substring += s[i]  

            for word in wordDict : 
                if substring == word : 
                    if self.wordBreak(s[len(substring):],wordDict) : 
                        return True 
                else : 
                    continue 
        return False 


        