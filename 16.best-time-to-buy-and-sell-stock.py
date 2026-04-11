class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        min_price = prices[0]

        for i in range(1, n):
            curr_profit = prices[i] - min_price
            if curr_profit > profit:
                profit = curr_profit
            min_price = min(min_price, prices[i])
        return profit