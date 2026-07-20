class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(start, s):
            if s == target:
                res.append(path[:])
                return

            if start >= len(nums) or s > target:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i, s + nums[i])
                path.pop()
        
        dfs(0, 0)
        return res