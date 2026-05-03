# Problem: Delete Operation for Two Strings
# URL: https://leetcode.com/problems/delete-operation-for-two-strings/
# Language: python3

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #Insertion=> len(word2)-LCS
        #Deletion=> len(word1)-LCS
        m=len(word1)
        n=len(word2)
        #Space Optimization
        cur=[0]*(n+1)
        prev=[0]*(n+1)
        for i in range(1,m+1):
            cur[0]=0
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    cur[j]=1+prev[j-1]
                else:
                    cur[j]=max(cur[j-1],prev[j])
            prev=cur
            cur=[0]*(n+1)
        return (m+n)-2*prev[n] 

        # dp=[[0]*(n+1) for _ in range(m+1)]
        # for i in range(1,m+1):
        #     for j in range(1,n+1):
        #         if word1[i-1]==word2[j-1]:
        #             dp[i][j]=1+dp[i-1][j-1]
        #         else:
        #             dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        # return (m+n)-2*dp[m][n]