class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Stock Market, prices
        # choose a day to buy, and sell in future
        # Return maximum profit

        # fixed window, variable window

        # Naive approach
        # 1. Buy a stock at ith day
        # 2. Sell the stock, the price should be more than buy price
        # invariant: the sell price is always higher than buy price
        # key idea: check all possible profits by selling in the future 
        #           and settle for max profit. Here i

        profit = 0

        # [3,4,1] - ith day
        # First get the smallest number

        # have two pointers, they both start on same day
        # if they are same unchanged
        # increment the right pointer
        # Compare if l < r then get the profit
        # else change the r with l, increment the right
        # calculate the max of profit 

        l = 0
        r = 0
        n = len(prices)

        # [10,1,5,6,7,1]
        # [10,8,7,5,2]
        while r < n:
            if prices[l] > prices[r]:
                l = r
            else:
                profit = max(profit, prices[r] - prices[l])
            
            r+=1
        
        return profit

        

         
        


        