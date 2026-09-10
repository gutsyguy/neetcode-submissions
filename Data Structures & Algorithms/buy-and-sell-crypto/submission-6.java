class Solution {
    public int maxProfit(int[] prices) {
        int l = 0;
        int profit = 0;
        int current_profit;

        for (int r = 0; r < prices.length; r++){
            current_profit = prices[r] - prices[l];
            if (current_profit > profit){
                profit = current_profit;
            }
            while (prices[l] > prices[r]){
                l += 1;
                current_profit = prices[r] - prices[l];
                if (current_profit > profit){
                    profit = current_profit;
                }   
            }
        }
        return profit;
    }
}
