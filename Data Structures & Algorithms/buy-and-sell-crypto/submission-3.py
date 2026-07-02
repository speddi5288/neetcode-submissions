class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0 

        while l < len(prices) and r < len(prices):
            while l < r and prices[l] >= prices[r]:
                l += 1
            if l == r:
                r += 1
            if r < len(prices) and prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
                r += 1
        
        return max_profit


        