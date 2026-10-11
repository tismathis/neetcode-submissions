class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        row, col = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(i, j, visited, prev_height):
            if i < 0 or i >= row or j < 0 or j >= col:
                return

            if (i, j) in visited:
                return

            currHeight = heights[i][j]

            if currHeight < prev_height:
                return

            visited.add((i, j))

            dfs(i - 1, j, visited, currHeight)
            dfs(i, j + 1, visited, currHeight)
            dfs(i + 1, j, visited, currHeight)
            dfs(i, j - 1, visited, currHeight)

        for i in range(row):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, col - 1, atlantic, heights[i][col - 1])

        for j in range(col):
            dfs(0, j, pacific, heights[0][j])
            dfs(row - 1, j, atlantic, heights[row - 1][j])

        return [[a, b] for a, b in pacific & atlantic]