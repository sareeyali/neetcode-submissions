class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if  not n:
            return True
        
        adj = {i : [] for i in range(n)}
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        seen = set()

        def dfs(i, par):
            if i in seen:
                return False
            
            seen.add(i)

            for nei in adj[i]:        
                if nei == par:
                    continue
                if not dfs(nei, i):
                    return False
            return True

        return dfs(0, None) and len(seen) == n
        