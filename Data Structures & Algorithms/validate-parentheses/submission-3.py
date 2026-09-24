class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Map = {"}" : "{}",")" : "(" , "]" : "["}

        for letter in s : 
            if s in Map.values() :
                stack.push(s)
            if s in Map.keys() :
                if Map(s) != stack.pop() :
                    return False
        return True