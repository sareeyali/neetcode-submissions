class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        for src, des in tickets:
            heapq.heappush(adj[src], des)

        path = []

        def dfs(curr):
            while adj[curr]:
                nxt = heapq.heappop(adj[curr])
                dfs(nxt)
            path.append(curr)

        dfs("JFK")
        return path[::-1]