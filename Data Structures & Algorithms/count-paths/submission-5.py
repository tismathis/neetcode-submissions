class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}   # (i, j) -> number of paths

        def recursion(i, j):
            if (i, j) in memo:          # already computed? reuse it
                return memo[(i, j)]

            if i < 0 or j < 0:
                result = 0
            elif i == 0 and j == 0:
                result = 1
            else:
                result = recursion(i - 1, j) + recursion(i, j - 1)

            memo[(i, j)] = result       # remember it for next time
            return result

        return recursion(m - 1, n - 1)