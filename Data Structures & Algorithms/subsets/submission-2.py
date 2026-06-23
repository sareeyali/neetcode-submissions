class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def dfs(i):
            if i == len(nums):
                res.append(path[:])
                return

            # choose the number
            path.append(nums[i])
            dfs(i+1)

            # skip the number
            path.pop()
            dfs(i+1)
        dfs(0)
        return res