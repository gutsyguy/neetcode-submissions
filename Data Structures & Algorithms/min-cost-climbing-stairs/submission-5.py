class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        memo = {}
        

        def helper(i):
            if i in memo:
                return memo[i]
            elif i >= n:
                return 0
            else:
                curr_cost = cost[i] + min(helper(i+1), helper(i+2))
                memo[i] = curr_cost
                return curr_cost

        return min(helper(0), helper(1)) 

        