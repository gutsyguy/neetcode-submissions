class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        l = 0
        for r in range(l+1, len(prices)):
            current_profit = prices[r] - prices[l]
            profit = max(profit, current_profit)
            while prices[l] > prices[r] and l < r:
                l += 1
                current_profit = prices[r] - prices[l]
                profit = max(profit, current_profit)
        
        return profit

            
            

        
        