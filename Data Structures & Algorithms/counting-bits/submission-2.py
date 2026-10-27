class Solution:
    def countBits(self, n: int) -> List[int]:

        counter = []

        for i in range(n) : 
            
            counterOf1 = 0

            for j in range(32) : 
                while (1 << j ) & i :
                    counterOf1  +=1
                    j +=1
                counter[i] = counterOf1
        return counter 
            
        