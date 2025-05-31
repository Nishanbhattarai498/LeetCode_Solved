from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        # Convert 1D index to 2D (row, col) in boustrophedon order
        def get_position(s):
            r = n - 1 - (s - 1) // n
            c = (s - 1) % n
            if (n - 1 - r) % 2 == 1:
                c = n - 1 - c
            return r, c

        visited = set()
        q = deque()
        q.append((1, 0))  # (square, move_count)

        while q:
            square, move = q.popleft()
            if square == n * n:
                return move

            for i in range(1, 7):
                next_square = square + i
                if next_square > n * n:
                    continue
                r, c = get_position(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                if next_square not in visited:
                    visited.add(next_square)
                    q.append((next_square, move + 1))

        return -1
