class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row,col = len(grid) , len(grid[0])


        def dfs(i,j) : 
            if (i<0 or i >= len(grid) or j < 0 or  j >= len(grid[0])) :
                return 
            if grid[i][j] == "0" :
                return 
            
            else : 
            
                grid[i][j] = "0" #don't visit the current node 
                #i need smth to track the number of islands ?? 


                dfs(i+1,j)
                dfs(i-1,j) #do the recursive calls 
                dfs(i,j+1)
                dfs(i,j-1)
    
        compteur = 0 
        for i in range (row) : 
            for j in range (col):
                if grid[i][j] == "1" :
                    compteur +=1
                    dfs(i,j)
        return compteur 
 
            