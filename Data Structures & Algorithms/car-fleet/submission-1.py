class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []

        tabSort = sorted(zip(position,speed),reverse = True) #sorte de maniere decroissante par rapport aux positions !! 
        

        for pos,speedI in tabSort :

            temps = (target-pos)//speedI

            if temps > stack.top() : 
                stack.append(temps) 
            else :
                continue 
        return len(stack)

            





            

