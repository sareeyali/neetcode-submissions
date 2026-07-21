class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(r, c):
            if (r < 0 or r >= m or c < 0
             or c >= n or grid[r][c] == "0"):
                return 0

            # mark visited
            grid[r][c] = "0"

            for dr, dc in dirs:
                bfs(dr + r, dc + c)

        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    res += 1
                    bfs(r, c)

        return res
                    