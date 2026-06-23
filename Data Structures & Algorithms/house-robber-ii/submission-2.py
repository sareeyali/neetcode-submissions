class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        if not nums:
            return 0

        '''
        if len(nums) == 1:
            return nums[0]

        def r(nums):
            prev1, prev2 = 0, 0
            for n in nums:
                temp = max(prev1, prev2 + n)
                prev2 = prev1
                prev1 = temp
            return prev1

        first = r(nums[1 :])
        second = r(nums[: -1])
        return max(first, second)