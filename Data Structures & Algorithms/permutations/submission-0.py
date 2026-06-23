class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        i = 0
        def backtrack(i):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for j in range(len(nums)):
                if nums[j] in path:
                    continue
                path.append(nums[j])
                backtrack(j)
                path.pop()
        backtrack(0)
        return res
