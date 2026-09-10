class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        stored = {}

        def helper(n):
            if n in stored:
                return stored[n]
            elif n > len(cost) - 1:
                return 0
            else:
                stored[n] = min(cost[n] + helper(n+1), cost[n] + helper(n+2))
                return min(cost[n] + helper(n+1), cost[n] + helper(n+2))

        return min(helper(1), helper(0))
                



        