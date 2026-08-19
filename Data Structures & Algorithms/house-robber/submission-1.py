class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0

        for n in nums:
            # one + n is skipping house two
            # two is skipping n
            # get max of those
            temp = max(one + n, two)
            one = two
            two = temp
        return two
