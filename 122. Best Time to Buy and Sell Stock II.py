class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        
        for idx in range(0, len(prices) - 1):
            if prices[idx + 1] > prices[idx]:
                maxProfit += prices[idx + 1] - prices[idx]
        
        return maxProfit
