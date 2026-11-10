class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        #the goal is to do a bin search in the lists and with the first element : 


        i,j = 0,len(matrix)-1 

        while i <= j : 

            m = i + (j-i)//2 

            if matrix[m][0] > target : 
                j = m-1 
            elif target > matrix[m][-1] : 
                i = m+1 
            else : 
                break
        else : 
            return False 
        
        row = matrix[m]
        l,r = 0,len(row)-1

        while l <= r : 
            mid = l + (r-l)//2 

            if row[mid] == target : 
                return True 
            elif row[mid] < target : 
                l = mid + 1 
            else : 
                r = mid - 1
        return False 


        