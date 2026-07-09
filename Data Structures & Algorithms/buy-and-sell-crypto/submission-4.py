class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minC = prices[0]
        maxP = 0
        for p in prices:
            minC = min(minC, p)
            maxP = max(maxP, p - minC)
        return maxP
            