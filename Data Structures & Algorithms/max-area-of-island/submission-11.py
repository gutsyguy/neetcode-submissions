class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        rows = len(grid)
        cols = len(grid[0])

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def bfs(row, col):
            curr = 1
            q = deque()
            q.append((row, col))
            grid[row][col] = 0

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = 0
                        curr += 1

            return curr

            

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    res = max(res, bfs(row, col))

        return res
        