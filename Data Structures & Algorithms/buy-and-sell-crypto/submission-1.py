class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        n = len(prices)
        maxProfit = 0

        for r in range(1, n): 

            if prices[l] < prices[r]:
                currProfit = prices[r] - prices[l]
                maxProfit = max(maxProfit, currProfit)

            elif prices[l] > prices[r]:
                l = r

        return maxProfit
            
