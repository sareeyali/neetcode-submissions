class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        
        pre = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            pre[c].append(p)
        seen = set()
        path = set()

        def dfs(c):
            if c in path:
                return False
            if c in seen:
                return True
            path.add(c)
            for p in pre[c]:
                if not dfs(p):
                    return False
            res.append(c)
            path.remove(c)
            seen.add(c)
            return True
            
        for c in range(numCourses):
            if not dfs(c): 
                return []
        return res
