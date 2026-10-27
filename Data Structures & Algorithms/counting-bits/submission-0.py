class Solution:
    def countBits(self, n: int) -> List[int]:

        counter = []

        for i in range(n) : 
            
            counterOf1 = 0

            while (n << j) & 1 :
                counterOf1  +=1
                j +=1
            counter[i] = counterOf1
        return counter 
            
        