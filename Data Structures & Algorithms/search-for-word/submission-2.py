class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()

        def dfs(r, c, idx):
            if idx == len(word):
                return True

            if 0 > r or r >= rows or 0 > c or c >= cols:
                return False
            # if not (0 <= r < rows and 0 <= c < cols):
            #     return False
            
            if (r, c) in visited:
                return False

            if board[r][c] != word[idx]:
                return False

            visited.add((r,c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if dfs(nr, nc, idx + 1):
                    return True

            visited.remove((r,c))

            return False

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False