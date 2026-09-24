class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        res = 0 


        def dfs(r, c):
            stack = []
            stack.append((r, c))
            visited.add((r,c))

            curr = 1

            while stack:
                row, col = stack.pop()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        stack.append((nr, nc))
                        visited.add((nr, nc))
                        curr += 1
            return curr

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    res = max(res, dfs(row, col))

        return res
        