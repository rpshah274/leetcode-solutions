# Problem: House Robber
# URL: https://leetcode.com/problems/house-robber/
# Language: python3

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp={}
        def solve(n):
            if n>=len(nums):
                return 0
            if n in dp:
                return dp[n]
            dp[n]= max(nums[n] + solve(n+2), solve(n+1))
            return dp[n]
        return solve(0)
