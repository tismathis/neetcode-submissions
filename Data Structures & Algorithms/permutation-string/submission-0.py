class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        tabs1 = [0] * 26
        tabs2 = [0] * 26
        length = len(s1)

        # count s1 and the first window of s2
        for k in range(length):
            tabs1[ord(s1[k]) - ord('a')] += 1
            tabs2[ord(s2[k]) - ord('a')] += 1

        if tabs1 == tabs2:
            return True

        # slide the window: j is the new right end, i is the char leaving
        for j in range(length, len(s2)):
            i = j - length
            tabs2[ord(s2[j]) - ord('a')] += 1   # add the new right character
            tabs2[ord(s2[i]) - ord('a')] -= 1   # remove the old left character
            if tabs1 == tabs2:
                return True

        return False
        