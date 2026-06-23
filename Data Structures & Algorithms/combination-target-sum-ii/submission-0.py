class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        c = sorted(candidates)
        res = []
        path = []
        i = 0

        def backtrack(i, curSum):
            if curSum == target:
                res.append(path[:])
                return
            if curSum > target:
                return
        
            for j in range(i, len(c)):
                if j > i and c[j] == c[j - 1]:
                    continue
                path.append(c[j])
                backtrack(j + 1, curSum + c[j])
                path.pop()

        backtrack(0, 0)
        return res