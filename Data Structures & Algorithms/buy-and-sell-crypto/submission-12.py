class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        i = 0
        j = 1
        while j < len(prices) :
            nextP = prices[j] - prices[i]
            if nextP > profit :
                profit = nextP
            if prices[j] < prices[i] :
                i = j
            else :
                j+=1
        return profit