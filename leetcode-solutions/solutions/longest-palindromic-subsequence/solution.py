# Problem: Longest Palindromic Subsequence
# URL: https://leetcode.com/problems/longest-palindromic-subsequence/
# Language: python3

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        s2=s[::-1]
        #Space Optimization
        cur=[0]*(n+1)
        prev=[0]*(n+1)
        for i in range(1,n+1):
            cur[0]=0
            for j in range(1,n+1):
                if s[i-1]==s2[j-1]:
                    cur[j]=1+prev[j-1]
                else:
                    cur[j]=max(cur[j-1],prev[j])
            prev=cur
            cur=[0]*(n+1)
        return prev[n]   
        # dp=[[0]*(n+1) for _ in range(n+1)]
        # for i in range(1,n+1):
        #     for j in range(1,n+1):
        #         if s[i-1]==s2[j-1]:
        #             dp[i][j]=1+dp[i-1][j-1]
        #         else:
        #             dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        # return dp[n][n]     