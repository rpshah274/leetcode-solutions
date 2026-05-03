# Problem: Longest Common Subsequence
# URL: https://leetcode.com/problems/longest-common-subsequence/
# Language: python3

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        #Space Optimization
        cur=[0]*(n+1)
        prev=[0]*(n+1)
        for i in range(1,m+1):
            cur[0]=0
            for j in range(1,n+1):
                if text1[i-1]==text2[j-1]:
                    cur[j]=1+prev[j-1]
                else:
                    cur[j]=max(cur[j-1],prev[j])
            prev=cur
            cur=[0]*(n+1)
        return prev[n] 
        # dp=[[0]*(n+1) for _ in range(m+1)]
        # for i in range(1,m+1):
        #     for j in range(1,n+1):
        #         if text1[i-1]==text2[j-1]:
        #             dp[i][j]=1+dp[i-1][j-1]
        #         else:
        #             dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        # return dp[m][n]