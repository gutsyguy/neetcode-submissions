class Solution:
    def climbStairs(self, n: int) -> int:
        stored = {}

        def climbStairsHelper(n):
            if n in stored:
                return stored[n]
            elif n < 4:
                return n
            else:
                stored[n] = climbStairsHelper(n-2) + climbStairsHelper(n - 1)
                return climbStairsHelper(n-2) + climbStairsHelper(n - 1)

        return climbStairsHelper(n)