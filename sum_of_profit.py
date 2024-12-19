class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSofar = prices[0]
        profit = 0

        for i in range (1, len(prices)):
            minSofar = min(minSofar, prices[i])
            if prices[i-1] < prices[i]:
                # profit = max(profit, prices[i]-minSofar)
                profit += (prices[i] - prices[i-1])

        return profit

