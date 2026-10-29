class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        res = 0
        counter = 0 
        for i in range(32) : 
            ##extract ith bit form both 
            if ((1 << i) & a and not ((1 << i) & b)) or ((1 << i) & b and not ((1 << i) & a)) : 
                if counter : 
                    res +=0 
            elif ((1 << i) & a) == 0 and ((1 << i) & b) == 0 : 
                if counter : 
                    res +=1 
            else : 
                counter +=1
                res +=1
            if counter : 
                res +=counter 
        return res 
