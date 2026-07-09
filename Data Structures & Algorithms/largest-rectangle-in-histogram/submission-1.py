class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(heights):
            l = i
            while stack and h < stack[-1][1]:
                curr = stack.pop()
                w = i - curr[0]
                res = max(res, curr[1] * w)
                l = curr[0]
            stack.append([l, h])
        
        for i, h in stack:
            res = max(res, h * (len(heights) - i))
        return res