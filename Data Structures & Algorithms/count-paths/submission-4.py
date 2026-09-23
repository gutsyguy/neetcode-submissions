class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        cols = n

        memo = [[-1] * cols for _ in range(rows)]

        def backtrack(i, j):
            if not (0 <= i < rows) or not (0 <= j < cols):
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            if i == (rows - 1) and j == (cols - 1):
                return 1

            else:
                memo[i][j] = backtrack(i + 1, j) + backtrack(i, j + 1)
                return memo[i][j]


        return backtrack(0,0)




        