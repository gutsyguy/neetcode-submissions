class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island_size = 0
        visited = set()

        rows = len(grid)
        cols = len(grid[0])

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            island_size = 1
            
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                        island_size += 1
                        grid[nr][nc] = 0
                        q.append((nr,nc))

            return island_size

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    max_island_size = max(max_island_size, bfs(r,c))

        return max_island_size
        