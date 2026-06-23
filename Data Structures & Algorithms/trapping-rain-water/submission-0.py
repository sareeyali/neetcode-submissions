class Solution:
    def trap(self, height: List[int]) -> int:
        ml = 0
        mr = 0
        l = 0
        r = len(height) - 1
        w = 0
        while l < r:
            cw = 0
            ml = max(ml, height[l])
            mr = max(mr, height[r])
            if ml < mr:
                cw = ml - height[l]
                l += 1
            else:
                cw = mr - height[r]
                r -= 1
            if cw > 0:
                w += cw

        return w

