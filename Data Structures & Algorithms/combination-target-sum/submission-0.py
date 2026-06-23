class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(i, curSum):
            if curSum == target:
                res.append(path[:])
                return

            if curSum > target:
                return

            for i in range(i, len(nums)):
                path.append(nums[i])
                backtrack(i, curSum + nums[i])
                path.pop()
                
        backtrack(0, 0)
        return res
