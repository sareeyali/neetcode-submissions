class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        curr = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or r >= rows 
            or c < 0 or c >= cols
            or word[i] != board[r][c] 
            or (r, c) in curr):
                return False

            curr.add((r, c))
            for dr, dc in dirs:
                if dfs(dr + r, dc + c, i + 1):
                    return True
            curr.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
