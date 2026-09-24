class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        islands = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]


        def dfs(r, c):
            stack = []
            stack.append((r, c))
            grid[r][c] = 0 

            while stack:
                row, col = stack.pop()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        stack.append((nr, nc))
                        grid[nr][nc] = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)

        return islands