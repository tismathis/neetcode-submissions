class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        #the goal is to do a bin search in the lists and with the first element : 


        i,j = 0,len(matrix)-1 

        while i < j : 

            m = i + (j-1)//2 

            if matrix[m][0] == target : 
                return True 

            elif matrix[m][0] < target and target > matrix[m][len(matrix[m])-1]: 
                i = m + 1 
            else : 
                j = m-1 
        