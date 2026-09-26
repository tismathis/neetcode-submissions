class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxim = 0

        for i in range(len(s)):
            HashMAP = {}                       # reset once per start i
            for j in range(i, len(s)):         # j goes from i to the end
                val = s[j]
                if val not in HashMAP:
                    HashMAP[val] = 1
                else:
                    HashMAP[val] += 1

                length = j - i + 1
                maxFreq = max(HashMAP.values())
                rep = length - maxFreq
                if rep <= k:                   # up to k replacements allowed
                    maxim = max(maxim, length)
        return maxim