class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit, gain = 0, 0
        for i in range(1, len(prices)):
            buy = min(buy, prices[i])
            if prices[i] - buy < profit:
                gain += profit
                buy = prices[i]
                profit = 0
            profit = max(profit, prices[i] - buy)
        gain += profit
        return max(gain, profit)
