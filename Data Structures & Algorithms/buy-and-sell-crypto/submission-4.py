class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        minBuy = 0
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[minBuy]:
                minBuy = i
            profit = max(profit, prices[i] - prices[minBuy])
        
        return profit