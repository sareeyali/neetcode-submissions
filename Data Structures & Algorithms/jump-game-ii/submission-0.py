class Solution:
    def jump(self, nums: List[int]) -> int:
        total = 0
        l = 0
        r = 0

        while r < len(nums) - 1:
            jump = 0
            for i in range(l, r + 1):
                jump = max(jump, nums[i])
            l = r + 1
            r += jump
            total += 1
        return total
