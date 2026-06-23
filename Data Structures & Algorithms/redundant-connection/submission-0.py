class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        
        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx != rooty:
                parent[rootx] = rooty
            
        for x, y in edges:
            if find(x) == find(y):
                return [x, y]
            union(x, y)