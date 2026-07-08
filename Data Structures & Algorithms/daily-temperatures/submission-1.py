class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                curr = stack.pop()
                res[curr[0]] = i - curr[0]
            stack.append([i, t])
        return res
            
