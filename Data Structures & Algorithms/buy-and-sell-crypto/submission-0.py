class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 # initialize profit
        for i in range(len(prices)):
            sell_price = prices[i]
            buy_price = min(prices[:i+1])
            profit = max(profit, sell_price - buy_price)
        return profit

        