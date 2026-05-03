# Problem: Climbing Stairs
# URL: https://leetcode.com/problems/climbing-stairs/
# Language: python3

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

        # dp={}
        # def solve(n):
        #     if n<0:
        #         return 0
        #     if n==0:
        #         return 1
        #     if n in dp:
        #         return dp[n]
        #     dp[n] = solve(n-1) + solve(n-2)
        #     return dp[n]
        # return solve(n)