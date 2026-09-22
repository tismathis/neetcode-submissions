class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        mult = 1;
        indexOfZero = 0;
        val = False;
        for i in nums :
            if i == 0 :
                indexOfZero = i
                val = True
            mult *=i

        res = [mult] * len(nums)

        for j in nums :
            if val :
                valeur=1
                res2 = [0] * len(nums)
                for i in nums : 
                    if i == indexOfZero :
                        continue
                    valeur *=i
                res2[indexOfZero] = valeur
                return res2
            else :
                res[j] /=j
        return res
