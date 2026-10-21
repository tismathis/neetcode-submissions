class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = amount + 1                 # more coins than could ever be needed
        dp = [0] + [INF] * amount        # dp[0] = 0: no coins for amount 0

        for x in range(1, amount + 1):
            for c in coins:
                if c <= x:
                    dp[x] = min(dp[x], dp[x - c] + 1)

        return dp[amount] if dp[amount] != INF else -1