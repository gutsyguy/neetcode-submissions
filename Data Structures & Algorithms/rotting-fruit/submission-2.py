class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0 
        q = deque()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    q.append((row, col))

        time = 0

        while q and fresh > 0:
            len_q = len(q)

            for _ in range(len_q):
                r, c = q.popleft()
        
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc <= col and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
                        
                
            time += 1

        return time if fresh == 0 else -1