class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # The L pointer will reperesent the day we buy a stock, while the R pointer will be the day we sell
        L, R = 0, 1

        maxProfit = 0

        while R < len(prices):
            if prices[L] < prices[R]:
                profit = prices[R] - prices[L]
                maxProfit = max(maxProfit, profit)
            else:
                L = R
            R += 1
        return maxProfit

