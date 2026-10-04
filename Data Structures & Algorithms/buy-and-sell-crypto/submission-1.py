class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price_idx = 0
        max_profit = 0

        for i in range (0, len(prices)):
            if i == 0:
                continue
            
            profit = prices[i] - prices[lowest_price_idx]
            max_profit = max(max_profit, profit)

            if prices[i] < prices[lowest_price_idx]:
                lowest_price_idx = i

        return max_profit