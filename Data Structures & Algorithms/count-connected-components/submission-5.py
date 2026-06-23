class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        root = [i for i in range(n)]

        def find(x):
            while root[x] != x:
                x = root[x]
            return x

        def union(x, y):
            parentx = find(x)
            parenty = find(y)
            if parentx != parenty:
                root[parenty] = parentx
                return True
            return False

        count = n

        for x, y in edges:
            if union(x, y):
                count -= 1

        return count