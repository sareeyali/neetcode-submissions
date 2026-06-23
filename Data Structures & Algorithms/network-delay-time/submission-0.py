class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, d in times:
            edges[u].append((d, v))

        heap = [(0, k)]
        seen = set()
        t = 0

        while heap:
            d1, n1 = heapq.heappop(heap)
            if n1 in seen:
                continue
            seen.add(n1)
            t = d1

            for d2, n2 in edges[n1]:
                if n2 not in seen:
                    heapq.heappush(heap, (d1 + d2, n2))

        return t if len(seen) == n else -1