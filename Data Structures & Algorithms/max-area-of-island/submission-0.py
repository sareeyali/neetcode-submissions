class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        area = 0
        seen = set()

        def dfs(r, c):
            if (r < 0 or r >= rows or
            c < 0 or c >= cols or
            (r, c) in seen or
            grid[r][c] == 0):
                return 0
            seen.add((r, c))
            return (1 + dfs(r + 1, c) + 
                        dfs(r - 1, c) + 
                        dfs(r, c + 1) + 
                        dfs(r, c - 1))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    area = max(area, dfs(r,c))
        return area

        
