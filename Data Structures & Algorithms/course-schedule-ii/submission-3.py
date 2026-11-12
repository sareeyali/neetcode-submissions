class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        deg = [0] * numCourses

        for c, p in prerequisites:
            adj[p].append(c)
            deg[c] += 1

        res = [i for i in range(numCourses) if deg[i] == 0]

        for u in res:
            for v in adj[u]:
                deg[v] -= 1
                if deg[v] == 0:
                    res.append(v)

        return res if len(res) == numCourses else []





