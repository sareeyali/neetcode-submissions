class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = 1
        for n in nums:
            if n == 0:
                return 0
            prod *= n
        if prod < 0:
            return -1
        else:
            return 1