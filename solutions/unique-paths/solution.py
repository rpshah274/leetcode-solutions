# Problem: Unique Paths
# URL: https://leetcode.com/problems/unique-paths/
# Language: python3

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1]*(n+1) for _ in range(m+1)]
        def solve(i,j):
            if i==m-1 and j==n-1:
                return 1
            if i<0 or j<0 or i>=m or j>=n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j]=solve(i+1,j) + solve(i,j+1)
            return dp[i][j]
        return solve(0,0)