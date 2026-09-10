class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        seen = set()

        islands = 0

        def bfs(row, col):
            q = deque()
            q.append((row,col))
            seen.add((row, col))

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc 

                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1" and (nr, nc) not in seen:
                        seen.add((nr,nc))
                        q.append((nr, nc))



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in seen:
                    bfs(row, col)
                    islands += 1

        return islands
        