class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0
        n = len(prices)

        for r in range(n):
            if prices[r] < prices[l]:
                l = r
            profit = max(profit, prices[r] - prices[l])

        return profit
        