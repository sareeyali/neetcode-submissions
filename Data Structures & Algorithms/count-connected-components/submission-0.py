class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = { i : [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        seen = set()
        count = 0

        def dfs(i):
            if i in seen:
                return
            seen.add(i)
            for nei in adj[i]:
                dfs(nei)

        for i in range(n):
            if i not in seen:
                dfs(i)
                count += 1

        return count

            

