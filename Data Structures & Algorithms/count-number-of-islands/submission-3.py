class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # visited = set()
        islands = 0

        rows = len(grid)
        cols = len(grid[0])

        def bfs(r,c):
            q = deque()
            q.append((r,c))

            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr,nc = row + dr, col + dc

                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        q.append((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    bfs(r,c)
                    islands += 1

        return islands
        