# Problem: Climbing Stairs II
# URL: https://leetcode.com/problems/climbing-stairs-ii/
# Language: python3

from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        prev3,prev2,prev1=0,0,0
        for c in costs:
            prev3,prev2,prev1=prev2,prev1,min(prev3+9,prev2+4,prev1+1) +c
        return prev1

        # dp = {}
        # def solve(i):
        #     if i == n:
        #         return 0
        #     if i in dp:
        #         return dp[i]
        #     ans = float('inf')
        #     for k in [1, 2, 3]:
        #         j = i + k
        #         if j <= n:
        #             ans = min(ans, costs[j-1] + k**2 + solve(j))
        #     dp[i] = ans
        #     return ans
        # return solve(0)