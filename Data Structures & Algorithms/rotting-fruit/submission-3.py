class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0

        rows = len(grid)
        cols = len(grid[0])
        timer = 0

        q = deque()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    q.append((row, col))

        while q and fresh > 0:
            len_q = len(q)

            for _ in range(len_q):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

            timer += 1

        return timer if fresh == 0 else -1





