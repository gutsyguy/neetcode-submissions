class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh  = 0
        minutes = 0
        q = deque()
        directions = [[1,0], [-1,0], [0,1],[0,-1]]

        rows = len(grid)
        cols = len(grid[0])

        if rows == 0:
            return 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))

        while q and fresh > 0:

            minutes += 1

            for _ in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                        q.append((nr,nc))
                        grid[nr][nc] = 2
                        fresh -= 1

        return -1 if fresh != 0 else minutes
        
        