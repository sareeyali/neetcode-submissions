class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        total = 0

        def bfs(r, c):
            q = collections.deque()
            seen.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in dir:
                    r, c = row + dr, col + dc
                    if ((r) in range(rows) and
                        (c) in range(cols) and 
                        grid[r][c] == "1" and
                        (r, c) not in seen):
                        q.append((r, c))
                        seen.add((r, c))
            return

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in seen:
                    bfs(r, c)
                    total += 1
        return total
    