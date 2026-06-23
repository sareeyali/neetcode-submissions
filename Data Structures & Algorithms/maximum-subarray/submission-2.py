class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        sum = nums[0]
        for n in nums:
            curr = max(0, curr)
            curr += n
            sum = max(curr, sum)
        return sum
