class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        if not edges : 
            return n

        adj = {i:[] for i in range(n)}

        counter = 0 
        visited = set()

        for i,j in edges : 
            adj[i].append(j)
            adj[j].append(i)

        def dfs(i) :
            
            if i not in visited :
                counter +=1 
                for j in adj[i] :
                     dfs(j) 
            
        return dfs(0)

            
            