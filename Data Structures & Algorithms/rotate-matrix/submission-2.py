class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        for col in range(len(matrix)-1) : 
            for row in range(len(matrix[0])-1) :

                matrix[col][row] = matrix[len(matrix)-col-1][row] #on fait l'echange de lignes 
        #transpose 

        for col in range(len(matrix)-1) : 
            for row in range(len(matrix[0])-1) : 
                matrix[col][row] = matrix[row][col]
        return matrix 

        