class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brutal force, time_out!
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, l):
        #         profit = prices[j] - prices[i]
        #         if profit > max_profit:
        #             max_profit = profit
        # return max_profit  
        
        # one pass
        min_price = math.inf
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit
