class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        res = 0
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c):
            if (r < 0 or r >= n  or c < 0 
            or c >= m or grid[r][c] != "1"):
                return 0
            grid[r][c] = "0"

            for dr, dc in dirs:
                dfs(dr + r, dc + c)
            
        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r, c)
        return res
         