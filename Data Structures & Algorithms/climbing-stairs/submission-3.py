class Solution:
    def climbStairs(self, n: int) -> int:
        seen = {}

        def helper(n):
            if n in seen:
                return seen[n]
            elif n < 4:
                return n
            else:
                curr = helper(n-1) + helper(n-2)
                seen[n] = curr
                return curr

        return helper(n)