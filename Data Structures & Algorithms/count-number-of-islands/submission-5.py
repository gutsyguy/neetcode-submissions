class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        islands = 0

        def bfs(row, col):
            q = deque()
            q.append((row,col))
            # seen.add((row, col))

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc 

                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1":
                        # seen.add((nr,nc))
                        grid[nr][nc] = "0"
                        q.append((nr, nc))



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    bfs(row, col)
                    grid[row][col] = "0"
                    islands += 1

        return islands
        