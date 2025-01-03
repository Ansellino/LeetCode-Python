
#
# Note: The class, method and parameter have been specified. Please do not modify
#
#
# 
# @param prices Integer One-dimensional Array Prices of stock in n day
# @return Integer
#
class Solution:
    def maxProfit(self, prices) :
        # write code here
        buy = prices[0]
        profit = 0
        for price in prices:
            if(buy > price):
                buy = price
            current_profit = price - buy
            if current_profit > profit:
                profit = current_profit

        return profit
