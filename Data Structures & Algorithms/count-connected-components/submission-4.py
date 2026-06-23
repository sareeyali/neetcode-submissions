class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        root = [i for i in range(n)]

        def find(x):
            while root[x] != x:
                x = root[x]
            return x

        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx != rooty:
                root[rooty] = rootx
                return True
            return False

        count = n

        for x, y in edges:
            if union(x, y):
                count -= 1

        return count