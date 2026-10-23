class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        substring = "" 
        for i in range(len(s)) : 

            substring += s[i]  

            for word in wordDict : 
                if substring == word : 
                    return self.wordBreak(s[len(substring):],wordDict)
                else : 
                    continue 
        if substring == word :
            return True 
        return False 


        