class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        if len(prices) < 2:
            return 0
        buy = prices[0]
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i+1] - buy > profit:
                profit = prices[i+1] - buy
            if prices[i+1] < buy:
                buy = prices[i+1]
        return profit