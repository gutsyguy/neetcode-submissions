class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island_size = 0

        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            island_size = 1

            direction = [[1,0],[-1,0], [0,1], [0,-1]]

            # for dr, dc in directions:
            while q:
                row, col = q.popleft()
                for dr, dc in direction:
                    nr = row + dr
                    nc = col + dc

                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1 and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr,nc))
                        island_size += 1
            
            return island_size




        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_island_size = max(bfs(r,c), max_island_size)
                    visited.add((r,c))

        return max_island_size
        