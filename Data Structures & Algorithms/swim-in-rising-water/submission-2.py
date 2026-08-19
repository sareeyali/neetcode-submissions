class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        res = 0
        heap = [[grid[0][0], 0, 0]]
        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        m = len(grid)
        n = len(grid[0])
        seen = set()
        seen.add((0, 0))

        while heap:
            h, r, c = heapq.heappop(heap)
            if (r == m - 1 and c == n - 1):
                return h
            for dr, dc in dirs:
                nr = dr + r
                nc = dc + c
                if (0 <= nr < m and 0 <= nc < n
                and (nr, nc) not in seen):
                    curH = max(h, grid[nr][nc])
                    seen.add((nr, nc))
                    heapq.heappush(heap, [curH, nr, nc])
        return -1
