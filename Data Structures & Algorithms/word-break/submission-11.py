class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}

        def helper(s):
            if s == "":
                return True
            if s in memo:
                return memo[s]

            for i in range(1, len(s) + 1):
                prefix = s[:i]
                if prefix in wordSet and helper(s[i:]):
                    memo[s] = True
                    return True

            memo[s] = False
            return False

        return helper(s)