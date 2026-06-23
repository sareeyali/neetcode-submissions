class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        i = 0
        nums.sort()
        def backtrack(i):
            if i <= len(nums):
                res.append(path[:])
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                path.append(nums[j])
                backtrack(j + 1)
                path.pop()
        backtrack(0)
        return res