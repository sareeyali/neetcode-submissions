class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        seen = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or 
            r >= m or c >= n or
            word[i] != board[r][c]
            or (r, c) in seen):
                return False

            seen.add((r, c))
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dr, dc in dirs:
                if dfs(r + dr, c + dc, i + 1):
                    return True

            seen.remove((r, c))
            return False

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0): 
                    return True
        return False