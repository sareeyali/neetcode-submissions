class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for i in range(n + 1)]
        seen = set()

        for u, v, t in times:
            adj[u].append((v, t))

        heap = [(0, k)]
        res = 0

        while heap:
            t1, n1 = heapq.heappop(heap)
            if n1 in seen:
                continue
            seen.add(n1)
            res = t1
            
            for n2, t2 in adj[n1]:
                if n2 not in seen:
                    heapq.heappush(heap, (t1 + t2, n2))
            
        return res if len(seen) == n else -1