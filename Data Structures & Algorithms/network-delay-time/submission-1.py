class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, d in times:
            adj[u].append((v, d))
        
        # make a heap
        heap = [(0, k)]

        seen = set()
        while heap:
            d, cur = heapq.heappop(heap)
            if cur in seen:
                continue
            seen.add(cur)
            if len(seen) == n:
                return d
            for nei, nd in adj[cur]:
                heapq.heappush(heap, (nd + d, nei))
        return -1




