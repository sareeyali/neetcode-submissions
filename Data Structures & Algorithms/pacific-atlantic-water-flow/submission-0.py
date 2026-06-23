class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        n = len(heights)
        m = len(heights[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # bfs function that accepts starts
        def bfs(starts):
            q = deque(starts)
            seen = [[False] * m for i in range(n)]

            for r, c in starts:
                seen[r][c] = True

            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr = dr + r
                    nc = dc + c
                    if (0 <= nr < n and 0 <= nc < m
                    and not seen[nr][nc] and
                    heights[nr][nc] >= heights[r][c]):
                        seen[nr][nc] = True
                        q.append((nr, nc))
            return seen
        
        # create starts
        pac = [(0, c) for c in range(m)] + [(r, 0) for r in range(n)]
        atl = [(n-1, c) for c in range(m)] + [(r, m-1) for r in range(n)]

        pacS = bfs(pac)
        atlS = bfs(atl)

        res = []
        for r in range(n):
            for c in range(m):
                if pacS[r][c] and atlS[r][c]:
                    res.append((r, c))
        
        return res