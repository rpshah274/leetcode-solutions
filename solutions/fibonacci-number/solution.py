# Problem: Fibonacci Number
# URL: https://leetcode.com/problems/fibonacci-number/
# Language: python3

class Solution:
    def fib(self, n: int) -> int:
        # dp={}#dictionary for O(1) lookup
        # #Recurion with memoization
        # def solve(n):
        #     if n==0:
        #         return 0
        #     if n==1:
        #         return 1
        #     if n in dp:
        #         return dp[n]
        #     dp[n]=solve(n-1)+solve(n-2)
        #     return dp[n]
        # return solve(n)
        if n <= 1:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]