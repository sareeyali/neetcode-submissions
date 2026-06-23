class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        seen = set()

        def dfs(c, prev):
            if c in seen:
                return False
            seen.add(c)
            for e in adj[c]:
                if e != prev and not dfs(e, c):
                    return False
            return True

        return dfs(0, -1) and len(seen) == n