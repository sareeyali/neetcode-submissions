class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        indegree = [0] * numCourses

        for c, p in prerequisites:
            adj[p].append(c)
            indegree[c] += 1

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        res = []
        
        while q:
            cur = q.popleft()
            res.append(cur)
            for nei in adj[cur]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)
                    
        if len(res) == numCourses:
            return res
        return []
