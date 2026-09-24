class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Map = {"}": "{", ")": "(", "]": "["}

        for letter in s:
            if letter in Map.values():
                stack.append(letter)
            elif letter in Map:
                if not stack or Map[letter] != stack.pop():
                    return False
        return not stack