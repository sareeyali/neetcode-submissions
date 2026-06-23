class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)
        i = 0
        def backtrack(i):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for j in range(len(nums)):
                if used[j]:
                    continue
                path.append(nums[j])
                used[j] = True
                backtrack(j)
                path.pop()
                used[j] = False
        backtrack(0)
        return res
