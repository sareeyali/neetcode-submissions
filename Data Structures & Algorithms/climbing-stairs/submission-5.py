class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 2
        for i in range(n-2):
            tmp = one + two
            one = two
            two = tmp
        return two