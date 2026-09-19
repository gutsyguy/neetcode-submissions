class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        rows = len(grid)
        cols = len(grid[0])

        max_size = 0

        def bfs(r, c):
            size = 1
            q = deque()
            grid[r][c] = 0
            q.append((r,c))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = 0
                        size += 1

            return size


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_size = max(bfs(row, col), max_size)


        return max_size

        
        