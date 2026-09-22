class Solution:
    def maxScore(self, s: str) -> int:
        total_ones = s.count("1")

        zero_left = 0;
        ones_left = 0;
        best = 0;
        for i in range (len(s)-1) :
            if s[i] == "0":
                zero_left +=1
            else :
                ones_left +=1
            ones_right = total_ones-ones_left
            score = zero_left + ones_right

            best = max(best,score)
            return best 

