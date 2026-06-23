class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = 0
        sell_price = 0
        profit = 0
        for i in range(len(prices) - 1, 0, -1):
            sell_price = max(sell_price, prices[i])
            buy_price = min(prices[:i])
            profit = max(profit, sell_price - buy_price)
        return profit

            