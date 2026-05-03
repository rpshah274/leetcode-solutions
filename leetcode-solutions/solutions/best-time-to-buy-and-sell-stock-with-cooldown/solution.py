# Problem: Best Time to Buy and Sell Stock with Cooldown
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# Language: python3

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n=len(prices)
        memo={}
        def dfs(i,canbuy):
            if i>=n:
                return 0  
            if (i,canbuy) in memo:
                return memo[(i,canbuy)]
            cooldown=dfs(i+1,canbuy)
            if canbuy:
                buy = dfs(i+1, not canbuy) - prices[i]
                memo[(i, canbuy)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not canbuy) + prices[i]
                memo[(i, canbuy)] = max(sell, cooldown)
            return memo[(i,canbuy)]
        return dfs(0,True)