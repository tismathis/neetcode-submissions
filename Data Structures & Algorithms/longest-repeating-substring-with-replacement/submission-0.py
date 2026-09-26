class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxim = 0

        for i in range (len(s)) :
            for j,val in enumarate(s) :
                HashMAP = {} 
                if val not in HashMAP :
                    HashMAP[val] = 1
                else :
                    HashMAP[val] +=1
                
                length = j-i + 1 
                maxFreq = max(HashMAP.values())
                rep = length - maxFreq
                if rep < k :
                    maxim = max(maxim,length) 
        return maxim

                