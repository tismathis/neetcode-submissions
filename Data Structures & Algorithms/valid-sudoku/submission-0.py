class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        rows = [set() for i in range(len(board))]

        col = [set() for i in range(len(board[0]))] #we create a set for each col and row indexed 

        for i in range(len(board)) : 
            for j in range(len(board[0])) : 

                if board[i][j] in rows[i] or board[i][j] in col[j] : 
                    return False 
                rows[i].add(board[i][j]) 
                cols[j].add(board[i][j]) 

        return True 