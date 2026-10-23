class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordSet = set()

        for i in wordDict : 
            wordSet.add(i) 


        if s == "":
                return True 

        substring = "" 
        for i in range(len(s)) : 

            substring += s[i]  

            if substring in wordSet : 
                if self.wordBreak(s[len(substring):],wordDict) : 
                    return True 
                else : 
                    continue 
        return False 


        