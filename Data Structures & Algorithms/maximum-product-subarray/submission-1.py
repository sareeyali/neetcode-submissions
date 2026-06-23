class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin = 1
        curMax = 1
        for n in nums:
            temp = curMax
            curMax = max(curMax * n, n * curMin, n)
            curMin = min(curMin * n, n * temp, n)
            res = max(curMin, curMax, res)

        return res