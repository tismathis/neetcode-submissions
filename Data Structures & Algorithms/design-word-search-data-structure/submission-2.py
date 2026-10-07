class TrieNode :
    def __init__(self) :
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root 

        for c in word : 
            if c not in curr.children : 
                curr.children[c] = TrieNode()
            curr = curr.children[c] 
        return curr.endOfWord 

           
        

    def search(self, word: str) -> bool:
        
        def dfs(j,root) :
            curr = root 

            for i in range (len(word)) : 
                c = word[i] 
                if c == "." :
                    for child in curr.children.values() :
                        if dfs(i+1,child) : 
                            return True 
                    return False 
                else : 
                    if c not in curr.children :
                        return False 
                    curr = curr.children
            return curr.endOfWord 
        dfs(0,root)
        
