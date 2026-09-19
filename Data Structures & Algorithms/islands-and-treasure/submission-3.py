class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        q = deque()

        inf = 2147483647
        timer = 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col))

        while q:
            len_q = len(q)

            for _ in range(len_q):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == inf:
                        grid[nr][nc] = min(grid[nr][nc], timer)
                        q.append((nr, nc))

            timer += 1
        
        
        

        
        