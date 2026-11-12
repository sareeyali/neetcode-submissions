class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        for s, d in tickets:
            heapq.heappush(adj[s], d)

        res = []

        def dfs(c):
            while adj[c]:
                d = heapq.heappop(adj[c])
                dfs(d)
            res.append(c)
        dfs('JFK')
        return res[::-1]
            
            
        
