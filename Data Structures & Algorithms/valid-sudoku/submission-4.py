class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        rows = [set() for i in range(len(board))]

        col = [set() for i in range(len(board[0]))] #we create a set for each col and row indexed

        boxes = [set() for i in range(len(board[0]//3)) for j in range(len(board))] #we create a set for each box of the sudoku 

        for i in range(len(board)) : 
            for j in range(len(board[0])) : 

                if board[i][j] in boxes[i//3][3 + (j//3)] : 
                    return False 

                if board[i][j] == "." : 
                    continue 

                if board[i][j] in rows[i] or board[i][j] in col[j] : 
                    return False 
                rows[i].add(board[i][j]) 
                col[j].add(board[i][j]) 

        return True 