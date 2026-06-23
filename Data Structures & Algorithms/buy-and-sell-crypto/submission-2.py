class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        opt = 0

        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
                continue
            profit = prices[i] - minPrice
            opt = max(opt, profit)
        return opt