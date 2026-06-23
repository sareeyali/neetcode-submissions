class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = collections.defaultdict(list) # i :[cost,  node]
        for p in points:
            for i in range(n):
                x1, y1 = points[i]
                for j in range(i + 1, n):
                    x2, y2 = points[j]
                    d = abs(x1 - x2) + abs(y1 - y2)
                    adj[i].append((d, j))
                    adj[j].append((d, i))

        #prims algo simple
        res = 0 # total cost of MST
        seen = set()
        heap = [(0, 0)] # cost goes first, thats how the min heap works
        while len(seen) < n:
            cost, node = heapq.heappop(heap)
            if node in seen:
                continue
            seen.add(node)
            res += cost
            for neiC, nei in adj[node]:
                if nei not in seen:
                    heapq.heappush(heap, (neiC, nei))

        return res