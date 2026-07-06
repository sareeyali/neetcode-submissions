class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minC = prices[0] # min cost
        maxP = 0 # max profit
        for p in prices:
            minC = min(minC, p)
            maxP = max(maxP, p - minC)
        return maxP