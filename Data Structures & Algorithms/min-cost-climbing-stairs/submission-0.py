class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step1 = 0
        step2 = 0
        for i in range(len(cost)):
            minP = cost[i] + min(step1, step2)
            step2 = step1
            step1 = minP
        return min(step1, step2)
            
