class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Stock Market, prices
        # choose a day to buy, and sell in future
        # Return maximum profit

        # fixed window, variable window

        # Naive approach
        # 1. Have two loops, first get the number
        # 2. Get next number it should be more the bought number

        profit = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1, len(prices)):
                if prices[j] > buy:
                    profit = max(profit, prices[j] - buy)
        
        return profit

        

         
        


        