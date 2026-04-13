class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0

        for i in range(1, n - 1):
            if prices[n + 1] > prices[i]:
                profit += prices[n + 1] - prices[i]
        return profit