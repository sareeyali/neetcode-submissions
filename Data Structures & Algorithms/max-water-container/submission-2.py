class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        opt = 0

        while l < r:
            height = min(heights[l], heights[r]) 
            area = height * (r - l)
            opt = max(opt, area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l +=1 
        return opt
        