from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):                        # matched the whole word
                return True
            if (r < 0 or r >= rows or c < 0 or c >= cols   # off the board
                    or board[r][c] != word[i]):            # wrong letter (or visited '#')
                return False

            tmp = board[r][c]
            board[r][c] = "#"                         # mark as visited

            found = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or
                     dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))

            board[r][c] = tmp                         # undo the mark
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False