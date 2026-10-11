

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        hashMap = {i : [] for i in range(numCourses)} 

        visitSet = set()

        for crs,req in prerequisites : 
            hashMap[crs].append(req)
        
        def dfs(crs) :
            if crs in visitSet : 
                return False #already visited 
            if hashMap[crs] == [] : 
                return True 

            visitSet.add(crs) #visited it 

            for req in hashMap[crs] : 
               if not dfs(req) : return False 
            visitSet.remove(crs)
            hashMap[crs] = []
            return True 
        for c in range(numCourses) :
            if not dfs(c) :
                return False 
        return True 
        
        

            
                
                    
                


        



        
        