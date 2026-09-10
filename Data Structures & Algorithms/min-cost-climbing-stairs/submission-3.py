class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def helper(n):
            if n > len(cost) - 1:
                return 0
            else:
                return min(cost[n] + helper(n+1), cost[n] + helper(n+2))

        return min(helper(1), helper(0))
                



        