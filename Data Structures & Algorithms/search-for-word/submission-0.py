def exist(self, board, word):
    rows, cols = len(board), len(board[0])

    def dfs(r, c, i):
        if i == len(word):            # matched the whole word?
            return True
        if i > len(word) or board[r][c] != word[i]:            # out of bounds or wrong letter?
            return False

        tmp = board[r][c]
        board[r][c] = "#"  # mark as visited

        found = (dfs(r+1,c,i) or dfs(r-1,c,i) or
                 dfs(r,c+1,i) or dfs(r,c-1,i))

        board[r][c] = tmp  # undo the mark
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False