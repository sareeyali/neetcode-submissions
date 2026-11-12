class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        path = set()
        for c, p in prerequisites:
            adj[c].append(p)

        def dfs(i):
            if i in path:
                return False
            if adj[i] == []:
                return True
            path.add(i)
            for c in adj[i]:
                if not dfs(c):
                    return False
            adj[i] = []
            path.remove(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
