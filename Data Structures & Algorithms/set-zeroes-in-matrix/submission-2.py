class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        visited = set(()) 
        
        for row in range(len(matrix)) : 
            for col in range(len(matrix[0])) : 

                if matrix[row][col]== 0 and (row,col) not in visited : 
                    #spread in 2 directions row and col !! and check if in visited 

                    for i in range(len(matrix[0])) : 
                        if (row,i) in visited : 
                            continue
                        set.add((row,i))
                        matrix[row][i] = 0 
                    for j in range(len(matrix)) : 
                        if (j,col) in visited : 
                            continue 
                        set.add((j,col)) 
                        matrix[j][col] = 0
                else : 
                    continue 
        return matrix 