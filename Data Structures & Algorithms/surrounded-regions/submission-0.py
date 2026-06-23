class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c):
            # base case
            if (r < 0 or c < 0 or r >= m or c >= n
            or board[r][c] != "O"):
                return 
            board[r][c] = "T"

            for dr, dc in dirs:
                dfs(dr + r, dc + c)
        # capture all edge regions to T for temp
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    if (r in [0, m - 1]
                    or c in [0, n - 1]):
                        dfs(r, c)

        # capture all surrounded regions O to X
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # uncapture unsupported regions T to O
        for r in range(m):
            for c in range(n):
                if board[r][c] == "T":
                    board[r][c] = "O"
