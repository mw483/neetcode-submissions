class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 # initialize profit
        min_buy = prices[0]
        for sell_price in prices:
            min_buy = min(min_buy, sell_price)
            max_profit = max(max_profit, sell_price - min_buy)
        return max_profit

        