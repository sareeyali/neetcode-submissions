class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i: [] for i in range(numCourses)}
        for cls, pre in prerequisites:
            premap[cls].append(pre)

        path = set()

        def dfs(cls):
            if cls in path:
                return False
            if premap[cls] == []:
                return True
                
            path.add(cls)
            for p in premap[cls]:
                if not dfs(p):
                    return False
            path.remove(cls)
            premap[cls] = []
            return True

        for cls in range(numCourses):
            if not dfs(cls): 
                return False
        return True 
        
