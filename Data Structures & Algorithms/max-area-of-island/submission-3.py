class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()

        rows = len(grid)
        cols = len(grid[0])

        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))

            curr_island = 1

            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r,c) not in visited:
                        curr_island += 1
                        visited.add((r,c))
                        q.append((r,c))

            return curr_island
                

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    visited.add((r,c))
                    max_area = max(max_area, bfs(r,c))

        return max_area