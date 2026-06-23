class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        minutes = 0
        m = len(grid)
        n = len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        q = collections.deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr = dr + r
                    nc = dc + c
                    if (0 <= nr < m and 0 <= nc < n and 
                    grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            if q:
                minutes += 1

        for r in grid:
                if 1 in r:
                    return -1
        return minutes


