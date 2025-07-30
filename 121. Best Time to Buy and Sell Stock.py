class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = max_profit = 0
        for i in range(1,len(prices)):
            profit = prices[i] - buy
            if profit < 0:
                buy = prices[i]
            else:
                max_profit = max(profit,max_profit)
        return max_profit
        
#Time Complexity: O(n)
#Space Complexity: O(1)
        