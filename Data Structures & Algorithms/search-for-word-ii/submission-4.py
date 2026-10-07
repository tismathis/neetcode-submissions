class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None          # the full word if one ends here

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:                      # your Trie building, unchanged
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.word = word

        rows, cols = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return                          # off the board
            letter = board[r][c]
            if letter not in node.children:     # also catches '#' (cell already used)
                return
            node = node.children[letter]
            if node.word:
                res.append(node.word)
                node.word = None                # avoid adding it twice
            board[r][c] = "#"                   # mark as used
            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)
            board[r][c] = letter                # backtrack

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        return res