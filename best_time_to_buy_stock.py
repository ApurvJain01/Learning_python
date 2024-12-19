class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        # i = 0
        # while i < len(prices) -1 :
        #     if prices[i] > prices[i+1]:
        #         return 0
        #     else:
        #         # profit_list = profit_list.append(prices[i+1] - prices[i])
        #         profit = max(profit, (profit[i+1]-profit[i]) )

        #     i += 1

        # return  profit 


        # for i in range(len(prices) - 1):
        #     for j in range (i + 1, len(prices)):
        #         profit = max(profit, (prices[j] - prices[i]))
        # return profit


        minSofar = prices[0]
        for i in range (1, len(prices)):
            minSofar = min(minSofar, prices[i])

            profit = max(profit, prices[i]-minSofar)
        return profit

