class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        islands = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = 0

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        q.append((nr, nc))
                        grid[nr][nc] = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    bfs(row, col)

        return islands