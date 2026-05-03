# Problem: Coin Change
# URL: https://leetcode.com/problems/coin-change/
# Language: python3

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if len(coins)==1 and amount%coins[0]!=0:
            return -1
        INF = float('inf')
        n=len(coins)
        dp=[[INF]*(amount+1) for _ in range(n+1)]
        for i in range(n + 1):
            dp[i][0] = 0
        for j in range(1,amount+1):
            if j%coins[0]==0:
                dp[1][j]= j//coins[0]
            else:
                dp[1][j]=float('inf')-1
        for i in range(2,n+1):
            for j in range(1,amount+1):
                if coins[i-1]<=j:
                    dp[i][j]=min(1+dp[i][j-coins[i-1]],dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        return -1 if dp[n][amount] == INF else dp[n][amount]

