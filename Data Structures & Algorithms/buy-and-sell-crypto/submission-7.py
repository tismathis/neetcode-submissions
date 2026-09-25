class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       profit = 0

       i = 0 
       j = 1 

       while i != j : 
            futureProfit = prices[j-1] - prices[i]
            if profit < futureProfit :
                profit = futureProfit 
            if prices[i] < prices[i-1] :
                i +=1
            elif prices[j-1] > prices[j-1] :
                j +=1
            else :
                j +=1 
                if (j == len(prices)-1) :
                    i +=1 
            return profit 
