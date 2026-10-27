from functools import lru_cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(maxsize=None)
        def recursion(i, j):
            if i < 0 or j < 0:
                return 0
            if i == 0 and j == 0:
                return 1
            return recursion(i - 1, j) + recursion(i, j - 1)

        return recursion(m - 1, n - 1)