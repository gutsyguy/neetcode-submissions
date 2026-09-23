from collections import deque

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        q = deque()

        # Start BFS from every cell containing word[0]
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    q.append((r, c, 0, {(r, c)}))

        while q:
            r, c, idx, visited = q.popleft()

            # We matched the entire word
            if idx == len(word) - 1:
                return True

            next_idx = idx + 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in visited
                    and board[nr][nc] == word[next_idx]
                ):
                    new_visited = visited.copy()
                    new_visited.add((nr, nc))

                    q.append(
                        (nr, nc, next_idx, new_visited)
                    )

        return False