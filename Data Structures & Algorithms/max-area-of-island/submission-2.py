class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island_length = 0
        # visited = set()

        rows = len(grid)
        cols = len(grid[0])

        def bfs(r,c):
            q = deque()
            max_length = 1

            q.append((r,c))
            # visited.add((r,c))

            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                        max_length += 1
                        # visited.add((r,c))
                        grid[r][c] = 0
                        q.append((r,c))

            return max_length
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # visited.add((r,c))
                    grid[r][c] = 0
                    max_island_length = max(max_island_length, bfs(r,c))

        return max_island_length

        

        