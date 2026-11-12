class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        deg = [0] * numCourses

        for c, p in prerequisites:
            adj[p].append(c)
            deg[c] += 1

        q = [i for i in range(numCourses) if deg[i] == 0]

        res = len(q)
        for u in q:
            for v in adj[u]:
                deg[v] -= 1
                if deg[v] == 0:
                    res += 1
                    q.append(v)
        return res == numCourses