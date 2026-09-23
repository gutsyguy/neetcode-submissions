class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * n

        def backtrack(n):
            if n <= 3:
                return n

            if dp[n - 1] != -1:
                return dp[n - 1]
            else:
                dp[n - 1] = backtrack(n - 1) + backtrack(n - 2)
                return dp[n - 1]
        # if n <= 3:
        #     return n

        # else:
        #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return backtrack(n)
        