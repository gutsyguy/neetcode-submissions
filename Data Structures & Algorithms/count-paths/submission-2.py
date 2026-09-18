class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if not i in range(n) or not j in range(m):
                return 0 

            if i == (n - 1) and j == (m - 1):
                return 1 

            memo[(i, j)] = dfs(i + 1, j) + dfs(i, j + 1)
            return memo[(i, j)]

        return dfs(0,0)
        