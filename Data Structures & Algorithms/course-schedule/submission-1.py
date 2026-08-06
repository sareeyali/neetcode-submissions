class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for c, p in prerequisites:
            indegree[c] += 1
            adj[p].append(c)
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        done = 0
        while q:
            cur = q.popleft()
            done += 1
            for nei in adj[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
                
        return done == numCourses