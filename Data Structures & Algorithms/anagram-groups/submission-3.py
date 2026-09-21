class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) 
        
        for str in strs : 
            const = [0] * 26
            for c in str : 
                const[ord(c)-ord('a')] +=1
            res[tuple(const)].append(str)
        return list(res.values())