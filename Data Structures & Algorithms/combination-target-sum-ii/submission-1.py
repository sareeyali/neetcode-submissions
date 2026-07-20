class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()

        def dfs(i, s):
            if s == target:
                res.append(path.copy())
                return
            
            if s > target:
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                path.append(candidates[j])
                dfs(j + 1, s + candidates[j])
                path.pop()

        dfs(0, 0)
        return res