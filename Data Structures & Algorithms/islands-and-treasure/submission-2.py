class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        seen = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        rows = len(grid)
        cols = len(grid[0])

        inf = 2147483647

        q = deque()
        distance = 1
        

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col))

        while q:
            len_q = len(q)

            for _ in range(len_q):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == inf:
                        grid[nr][nc] = min(grid[nr][nc], distance)
                        q.append((nr, nc))
            print(q)
                
            distance += 1

        