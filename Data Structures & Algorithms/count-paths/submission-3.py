class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]
        
        def backtrack(i, j):
            if not (0 <= i < m) or not (0 <= j < n):
                return 0 

            if memo[i][j] != -1:
                return memo[i][j]

            if i == (m - 1) and j == (n - 1):
                return 1

            else:
                memo[i][j] = backtrack(i + 1, j) + backtrack(i, j + 1)
                return memo[i][j]

        return backtrack(0,0)


        