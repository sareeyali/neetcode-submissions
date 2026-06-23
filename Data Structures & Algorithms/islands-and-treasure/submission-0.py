class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        q = collections.deque()
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if (0 <= nr < m and 0 <= nc < n
                and grid[nr][nc] > 0):
                    if grid[r][c] + 1 < grid[nr][nc]:
                        grid[nr][nc] = grid[r][c] + 1
                        q.append((nr, nc))