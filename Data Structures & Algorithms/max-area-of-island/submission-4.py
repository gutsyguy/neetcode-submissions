class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        rows = len(grid)
        cols = len(grid[0])

        def bfs(r,c):
            q = deque()
            q.append((r,c))

            curr_island = 1

            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                        curr_island += 1
                        grid[r][c] = 0
                        q.append((r,c))

            return curr_island
                

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    # visited.add((r,c))
                    max_area = max(max_area, bfs(r,c))

        return max_area