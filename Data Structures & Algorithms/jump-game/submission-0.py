class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        curr = goal
        while curr >= 0:
            if curr + nums[curr] >= goal:
                goal = curr
            curr -= 1
        return goal == 0