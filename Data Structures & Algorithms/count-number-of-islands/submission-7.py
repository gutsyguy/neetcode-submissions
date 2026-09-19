class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        rows = len(grid)
        cols = len(grid[0])

        islands = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def bfs(row, col):
            q = deque()
            seen.add((row, col))
            q.append((row, col))

            while q:
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and grid[nr][nc] == "1":
                        seen.add((nr, nc))
                        q.append((nr, nc))

        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in seen:
                    islands += 1
                    bfs(row, col)

        return islands
        