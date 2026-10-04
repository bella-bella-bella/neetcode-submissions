class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = [0] * len(prices)
        max_profit = 0

        for i in range (0, len(prices)):
            if i == 0:
                continue
            
            profit = prices[i] - prices[lowest[i - 1]]
            max_profit = max(max_profit, profit)

            if prices[i] < prices[lowest[i - 1]]:
                lowest[i] = i
            else:
                lowest[i] = lowest[i - 1]

        return max_profit