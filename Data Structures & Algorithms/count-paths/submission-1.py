class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            if i not in range(n) or j not in range (m):
                return 0
            if i == n - 1 and j == m - 1:
                return 1
            if memo[j][i] != -1:
                return memo[j][i]
            memo[j][i] = dfs(i + 1, j) + dfs(i, j + 1)
            return memo[j][i]

        return dfs(0,0)
        