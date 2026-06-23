class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
       n = len(grid)
       dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
       seen = set()
       heap = [(grid[0][0], 0, 0)]
       seen.add((0, 0))

       while heap:
        t, r, c = heapq.heappop(heap)
        seen.add((r, c))
        if r == n - 1 and c == n - 1:
            return t
        for dr, dc in dirs:
            nr = dr + r
            nc = dc + c
            if (nr < 0 or nr >= n 
            or nc < 0 or nc >= n
            or (nr, nc) in seen):
                continue
            seen.add((nr, nc))
            heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))
    